import os
import time
from pocketsphinx import LiveSpeech
from pydub import AudioSegment
from pydub.playback import play

# Set up the speech recognition configuration
config = {
    'verbose': False,
    'sampling_rate': 16000,
    'buffer_size': 2048,
    'no_search': False,
    'full_utt': False,
    'hmm': '/usr/share/pocketsphinx/model/en-us/en-us',  # acoustic model
    'lm': '/usr/share/pocketsphinx/model/en-us/en-us.lm.bin',  # language model
#    'dict': '/usr/share/pocketsphinx/model/en-us/cmudict-en-us.dict'  # dictionary
    'dict': './custom.dict'  # dictionary
}

# Define the trigger phrase
trigger_phrase = "first things first"

# Load the audio clip
audio_clip = AudioSegment.from_mp3("imtherealest.mp3")

def play_audio_clip():
    print("i'm the realest =3")
    play(audio_clip)

# Initialize the speech recognition object
speech = LiveSpeech(**config)

# Start listening for the phrase
for phrase in speech:
    if trigger_phrase in str(phrase).lower():
        print(phrase)
        play_audio_clip()

