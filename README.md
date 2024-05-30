# Whisper2Clipboard
A short Python script that talks to OpenAI's Whisper voice model to transcribe spoken words to text, then presents in the information for easy posting in Space Station 13.

This script has the following dependancies:
An Nvidia Graphics card with at least 2gb VRAM and some CUDA cores (you can use AMD GPUs or your CPU but you'll have to futz with the script and it may be slower than you expect.
Python 3.10.11
NVIDIA CUDA Runtime 11.8 (Latter versions play silly buggers)
Pytorch for CUDA 11.8 (cu118? idk I'm just a script kiddie)

## Installation
1: Download and Install Python 3.10.11. 
  By default, Python installs to C:\Users\%USERNAME%\AppData\Programs\Python\Python310

2: Install NVIDIA CUDA Runtime 11.8

3: Install Pytorch for CUDA 11.8. You can usually install it using the following command:
```bash
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```
