# Whisper2Clipboard
A short Python script that talks to OpenAI's Whisper voice model to transcribe spoken words to text, then presents in the information for easy posting in Space Station 13.

You'll need:
* A basic understanding of how to use a shell environment.
* An Nvidia Graphics card with at least 2gb VRAM and some CUDA cores (you can use AMD GPUs or your CPU but you'll have to futz with the script and it may be slower than you expect.
* Python 3.10.11
* NVIDIA CUDA Runtime 11.8 (Latter versions play silly buggers)
* Pytorch for CUDA 11.8 (cu118? idk I'm just a script kiddie)

## Installation
1. Download and Install Python 3.10.11.  
  By default, Python installs to `C:\Users\%USERNAME%\AppData\Programs\Python\Python310\`
2. Install NVIDIA CUDA Runtime 11.8
3. Install Pytorch for CUDA 11.8. You can usually install it using the following command in a shell prompt of your choice:
```bash
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```
4. Install FFMPEG and ensure the directory that contains the FFMPEG is added to the PATH Environment Variable.  
  Java's guide to doing this is located [here](https://www.java.com/en/download/help/path.html)  
  Ensure you are ADDING to the PATH variable, not overwriting it.   
6. Install OpenAI's Whisper model:
```bash
pip install git+https://github.com/openai/whisper.git
```
6. Install the script dependancies with the following commands typed into a shell prompt:
  ```bash
  pip install pyaudio
  pip install blobfile
  pip install pynput
  pip install pywin32
  ```
7. Create a folder in your `C:\users\%username%\Documents\` folder called **W2C**
8. Drop W2C.py and button.wav in this folder

## How to run W2C:
1. Open a shell prompt of your choice.  
  Personally, I use Powershell 7.
2. cd to your W2C folder in your Documents folder
3. Run the following command (or whatever flavor of python execution your computer is happy running)
  ```bash
  python W2C.py
  ```
4. How to exit W2C: Close the shell prompt or CTRL-C it. 

## Changing the behaviour of W2C

1. Open W2C.py in your favorite IDE
* If you don't like the 'I've finished transcribing' sound, delete line 119
* Listen and Post Keybindings are lines 25 and 26
* If you want Whisper to translate your spoken words to a different language, line 37 is your jam.

## Disclaimer
This software is provided as is. I'll do my best to keep this readme up to date, but I'm an amateur at best so please manage your expectations.

## Credits
A large portion of this script was flat out stolen from the following stack overflow page:  
https://stackoverflow.com/questions/44894796/pyaudio-and-pynput-recording-while-a-key-is-being-pressed-held-down  
The user that made the post is: Ron Norris  
https://stackoverflow.com/users/8093469/ron-norris  

A big thanks to Ron, you don't know this but your post from 7 years ago taught me a lot about python and I'm very grateful.   

Also OpenAI, for making such a great model. I hope that this script does right by you and that the licensing is all OK.
