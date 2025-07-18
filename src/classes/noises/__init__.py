import os


def get_wav_files():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    wav_files = {}
    
    for file in os.listdir(current_dir):
        if file.endswith(".wav"):
            file_name = os.path.splitext(file)[0]
            file_path = os.path.join(current_dir, file)
            wav_files[file_name] = file_path
    
    return wav_files


files = get_wav_files()
