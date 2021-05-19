from argparse import ArgumentParser
from pathlib import Path
import re
import soundfile as sf
import time
from vietTTS.nat.text2mel import text2mel
from vietTTS.hifigan.mel2wave import mel2wave
import uuid
import base64
import os
lexicon_file="assets/infore/lexicon.txt"
def nat_normalize_text(text):
    text = text.lower().strip()
    text = re.sub(r'[\n.,:]+', ' sp ', text)
    text = re.sub('[ ]+', ' ', text)
    return text.strip()
def gen_mel(text):
    text = nat_normalize_text(text)
    mel = text2mel(text,lexicon_file,0.2)
    return mel
def gen_wave(mel):
    wave = mel2wave(mel)
    return wave
def main(text):
    wave = gen_wave(gen_mel(text))
    output_path = str(uuid.uuid4()) + ".wav"
    sf.write(output_path, wave, samplerate=16000)
    encode_string = base64.b64encode(open(output_path, "rb").read())
    os.remove(output_path)
    return encode_string