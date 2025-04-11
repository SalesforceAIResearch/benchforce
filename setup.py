from setuptools import find_packages, setup

setup(
    name="benchforce",
    version="0.0.1",
    description="Benchforce",
    long_description=open("README.MD").read(),
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "websockets>=15.0.1",
        "python_dotenv>=1.1.0",
        "openai==1.65.4",
        "anthropic==0.49.0",
        "cartesia==1.4.0",
        "deepgram-sdk==3.10.1",
        "pandas>=2.2.3",
        "pydub>=0.25.1",
        "numpy>=2.2.4",
        "scipy>=1.15.2",
        "pyyaml>=6.0.2",
        "google-genai==1.9.0",
        "together==1.4.1",
        "tqdm==4.67.1",
    ],
)
