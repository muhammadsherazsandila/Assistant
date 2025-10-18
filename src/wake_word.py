import pvporcupine
import pyaudio
import struct
from dotenv import load_dotenv
import os

load_dotenv()

ACCESS_KEY = os.getenv("PORCUPINE_KEY")
WAKE_WORD = os.getenv("WAKE_WORD")

porcupine = pvporcupine.create(
    access_key=ACCESS_KEY,
    keywords=[WAKE_WORD]
)

pa = pyaudio.PyAudio()
audio_stream = pa.open(
    rate=porcupine.sample_rate,
    channels=1,
    format=pyaudio.paInt16,
    input=True,
    frames_per_buffer=porcupine.frame_length
)

def listen_for_wake_word():
    print("Listening for wake word...")
    while True:
        pcm = audio_stream.read(porcupine.frame_length, exception_on_overflow=False)
        pcm_unpacked = struct.unpack_from("h" * porcupine.frame_length, pcm)
        keyword_index = porcupine.process(pcm_unpacked)
        if keyword_index >= 0:
            print("Wake word detected!")
            return

