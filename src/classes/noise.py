from pydub import AudioSegment
from io import BytesIO
from src.classes.noises import files
import numpy as np
from scipy.signal import butter, filtfilt


class NoiseMixer:
    def __init__(
        self,
        noises: list[str],
        noise_volume: int,
        sample_rate: int,
        cutoff_freq: float,
        clipping_threshold: float,
        drop_probability: float,
        snr_db: float,
        chunk_size_ms: int,
    ):
        self.validate_noises(noises)
        self.noises = noises
        self.sample_rate = sample_rate
        self.cutoff_freq = cutoff_freq
        self.clipping_threshold = clipping_threshold
        self.drop_probability = drop_probability
        self.chunk_size_ms = chunk_size_ms
        self.snr_db = snr_db
        self.noise_volume = self.calculate_volume_adjustment(noise_volume)
        self.noise_segment = self.combine_noises(noises)

    def validate_noises(self, noises):
        missing_files = [name for name in noises if name not in files]
        if missing_files:
            raise FileNotFoundError(f"Missing noise files: {', '.join(missing_files)}")

    def calculate_volume_adjustment(self, noise_volume):
        if not (0 <= noise_volume <= 10):
            raise ValueError("noise_volume must be between 0 and 10")
        return (noise_volume - 5) * 2

    def combine_noises(self, noises):
        
        if not noises:
            return None
    
        noise_segments = [
            AudioSegment.from_file(files[name]).set_frame_rate(self.sample_rate)
            for name in noises
        ]

        max_length = max(len(n) for n in noise_segments)

        extended_noises = [self.loop_audio(n, max_length) for n in noise_segments]

        combined_noise = extended_noises[0]
        for noise in extended_noises[1:]:
            combined_noise = combined_noise.overlay(noise)

        combined_noise = combined_noise.apply_gain(self.noise_volume)

        return combined_noise

    def loop_audio(self, audio, target_length):
        repeats = (target_length // len(audio)) + 1
        looped_audio = audio * repeats
        return looped_audio[:target_length]

    def _audio_bytes_to_np(self, audio_bytes):
        audio = AudioSegment.from_raw(
            BytesIO(audio_bytes),
            sample_width=2,
            frame_rate=self.sample_rate,
            channels=1,
        )
        samples = np.array(audio.get_array_of_samples()).astype(np.float32)
        samples_norm = samples / 32768.0
        return samples_norm, audio

    def _np_to_audio_bytes(self, samples, audio_template):
        samples = np.clip(samples, -1, 1)
        samples_int16 = (samples * 32767).astype(np.int16)
        new_audio = AudioSegment(
            samples_int16.tobytes(),
            frame_rate=audio_template.frame_rate,
            sample_width=audio_template.sample_width,
            channels=audio_template.channels,
        )
        buffer = BytesIO()
        new_audio.export(buffer, format="wav")
        return buffer.getvalue()

    def apply_guassian_noise(self, audio_bytes):
        if self.snr_db <= 0:
            return audio_bytes

        samples, audio_template = self._audio_bytes_to_np(audio_bytes)
        signal_power = np.mean(samples**2)
        noise_power = signal_power / (10 ** (self.snr_db / 10))
        noise_std = np.sqrt(noise_power)
        noise = np.random.normal(0, noise_std, samples.shape)
        noisy_samples = samples + noise
        return self._np_to_audio_bytes(noisy_samples, audio_template)

    def apply_packet_loss(self, audio_bytes):
        if self.drop_probability <= 0 or self.chunk_size_ms <= 0:
            return audio_bytes

        samples, audio_template = self._audio_bytes_to_np(audio_bytes)
        chunk_samples = int(self.chunk_size_ms * self.sample_rate / 1000)
        if chunk_samples <= 0:
            return audio_bytes

        num_samples = len(samples)
        for start in range(0, num_samples, chunk_samples):
            if np.random.random() < self.drop_probability:
                end = min(start + chunk_samples, num_samples)
                samples[start:end] = 0
        return self._np_to_audio_bytes(samples, audio_template)

    def apply_clipping(self, audio_bytes):
        if self.clipping_threshold <= 0 or self.clipping_threshold >= 1:
            return audio_bytes

        samples, audio_template = self._audio_bytes_to_np(audio_bytes)
        clipped_samples = np.clip(
            samples, -self.clipping_threshold, self.clipping_threshold
        )
        return self._np_to_audio_bytes(clipped_samples, audio_template)

    def apply_low_pass_filtering(self, audio_bytes):
        if self.cutoff_freq <= 0:
            return audio_bytes

        samples, audio_template = self._audio_bytes_to_np(audio_bytes)
        nyquist = 0.5 * self.sample_rate
        normal_cutoff = self.cutoff_freq / nyquist
        if normal_cutoff >= 1.0:
            return audio_bytes
        order = 3
        b, a = butter(order, normal_cutoff, btype="low", analog=False)
        filtered_samples = filtfilt(b, a, samples)
        return self._np_to_audio_bytes(filtered_samples, audio_template)

    def apply_noise(self, audio_bytes):
        if not self.noises:
            return audio_bytes

        original_audio = AudioSegment.from_raw(
            BytesIO(audio_bytes),
            sample_width=2,
            frame_rate=self.sample_rate,
            channels=1,
        )

        noise_audio = self.noise_segment.set_sample_width(
            original_audio.sample_width
        ).set_channels(original_audio.channels)

        noise_audio = self.loop_audio(noise_audio, len(original_audio))

        mixed_audio = original_audio.overlay(noise_audio)

        audio_buffer = BytesIO()
        mixed_audio.export(audio_buffer, format="wav")

        return audio_buffer.getvalue()
    
    def apply(self, audio_bytes):
        audio_bytes = self.apply_noise(audio_bytes)
        audio_bytes = self.apply_low_pass_filtering(audio_bytes)
        audio_bytes = self.apply_clipping(audio_bytes)
        audio_bytes = self.apply_guassian_noise(audio_bytes)
        audio_bytes = self.apply_packet_loss(audio_bytes)

        return audio_bytes
        

