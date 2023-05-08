from dict import dict
# from dotenv import load_dotenv

import Ham2SIGML
import socket
import time
import os
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


def convert():
    with open('text.txt') as file:
        data = file.read().split()

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
        time.sleep(2)

convert() 
