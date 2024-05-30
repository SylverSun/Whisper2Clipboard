from pynput import keyboard
from pynput.keyboard import Key, Controller
import win32clipboard as winclip
import time
import pyaudio
import wave
import sched
import sys
import whisper
import winsound

#Our audio recording settings, leave these alone
CHUNK = 8192
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "output.wav"

#Select the Whisper model. We choose small so it's quick
model = whisper.load_model('small')

#Keybinds and the controller for activating recording and posting to chat
keyboardpresser = Controller()
LISTEN_KEY = keyboard.Key.shift_r
POSTIT_KEY = keyboard.Key.ctrl_r

#get the script thinking about audio, start from an empty slate
p = pyaudio.PyAudio()
frames = []

def callback(in_data, frame_count, time_info, status):
    frames.append(in_data)
    return (in_data, pyaudio.paContinue)

#push some settings to Whisper, we could make it speak another language if we wanted
def get_transcribe(audio: str, language: str = 'en'):
    return model.transcribe(audio=audio, language=language, verbose=False)

#How we proccess copying stuff to our clipboard
def copy_to_clipboard(text):
    winclip.OpenClipboard()
    winclip.EmptyClipboard()
    winclip.SetClipboardData(winclip.CF_UNICODETEXT, str(text))
    winclip.CloseClipboard()

#Detect and handle keypresses
class MyListener(keyboard.Listener):
    def __init__(self):
        super(MyListener, self).__init__(self.on_press, self.on_release)
        self.key_pressed = None
    def on_press(self, key):
        try:
            #if key.char == 'r':
            if key == LISTEN_KEY:
                self.key_pressed = True
            return True
        except:
            pass

    def on_release(self, key):
        try:
            #if key.char == 'r':
            if key == LISTEN_KEY:
                self.key_pressed = False
            elif key == POSTIT_KEY:
                print("We posted it :)")
                keyboardpresser.press('t')
                keyboardpresser.release('t')
                keyboardpresser.press(Key.ctrl_l)
                keyboardpresser.press('v')
                keyboardpresser.release('v')
                keyboardpresser.release(Key.ctrl_l)
            return True
        except:
            pass

#init the listener with default settings
listener = MyListener()
listener.start()
started = False
stream = None

#record and transcribe our audio
def recorder():
    global started, p, stream, frames
       
    if listener.key_pressed and not started:
        # start recording
        try:
            #set up  the recording from the start
            listener.wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
            listener.wf.setnchannels(CHANNELS)
            listener.wf.setsampwidth(p.get_sample_size(FORMAT))
            listener.wf.setframerate(RATE)
            stream = p.open(format=FORMAT,channels=CHANNELS,rate=RATE,input=True,frames_per_buffer=CHUNK,stream_callback = callback,input_device_index=1)
            print("Stream active:", stream.is_active())
            started = True
        except:
            raise

    elif not listener.key_pressed and started:
        #stop writing frames, close the wave file
        stream.stop_stream()
        stream.close()
        listener.wf.writeframes(b''.join(frames))
        listener.wf.close()
        result = get_transcribe(audio='./output.wav')
        print('-'*50)
        print(result.get('text', ''))
        #reset the keypress flags
        started = False
        stream = None
        frames = []
        #smash it into the clipboard, start from the top
        copy_to_clipboard(result.get('text', ''))
        print("Text copied successfully!")
        #play a sound so we know the text has finished being transcribed
        winsound.PlaySound("button.wav", winsound.SND_FILENAME)
        task.enter(0.1, 1, recorder, ())
    # run the recorder again
    task.enter(0.1, 1, recorder, ())


print("Press and hold the Right Shift key to begin recording")
print("Press the right CTRL key to queue up a post in SS13")
task = sched.scheduler(time.time, time.sleep)
task.enter(0.1, 1, recorder, ())
task.run()