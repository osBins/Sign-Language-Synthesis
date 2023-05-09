from dict import dict
# from dotenv import load_dotenv

import Ham2SIGML
import socket
import time
import os
import videototext as vt
# import psutil

# load_dotenv()
# PLAYER_PATH = os.environ.get("PLAYER_PATH")

# def processRunning(process):
#     for proc in psutil.process_iter():
#         try:
#             if process.lower() in proc.name().lower():
#                 return True
#         except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
#             pass
#     return False

# Uncomment to run Locally

# if processRunning('SiGML-Player'):
#     time.sleep(2)
# else:
#     os.startfile(PLAYER_PATH)
#     time.sleep(2)

def transcribeText(videoName):
    vt.convert_video_to_text("./videos/"+videoName, "./audios/audio-from-video.wav")

def convert(videoName):
    transcribeText(videoName)
    
    with open('result.txt') as file:
        data = file.read().split()

    with open("SiGML-output.sigml", "w") as f:
        f.write("""<?xml version="1.0" encoding="utf-8"?>\t
<sigml>\n""")
        
    for i in data:
        # handling HamNoSys encoding-decoding via Unicode characters
        if i not in dict:
            print(i, "is not in dictionary, continuing...")
            continue
        res = ''.join(r'\u{:04x}'.format(ord(chr)) for chr in dict[i])
        hamList = [res.encode().decode('unicode_escape')]
	    
        Ham2SIGML.readInput(hamList, i)

        # with open('SiGML-output.sigml', 'r') as file:
        #     s = socket.socket()
        #     s.connect(("localhost", 8052))
        #     data = file.read()
        #     s.sendall(bytes(data, encoding="utf-8"))
        time.sleep(0.5)
    with open("SiGML-output.sigml", "a") as f:
        f.write("""\n</sigml>""")