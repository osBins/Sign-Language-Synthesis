import Ham2SIGML
import socket
from dict import dict
import time
import os
from dotenv import load_dotenv
import psutil


load_dotenv()
PLAYER_PATH = os.environ.get("PLAYER_PATH")

def processRunning(process):
    for proc in psutil.process_iter():
        try:
            if process.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False;

if processRunning('SiGML-Player'):
    time.sleep(2)
else:
    os.startfile(PLAYER_PATH)
    time.sleep(2)


def convert():
    with open('text.txt') as file:
        data = file.read().split()

    for i in data:
        # handling HamNoSys encoding-decoding via Unicode characters
        res = ''.join(r'\u{:04x}'.format(ord(chr)) for chr in dict[i])

        hamList = [res.encode().decode('unicode_escape')]
        Ham2SIGML.readInput(hamList)
        
        with open('SiGML-output.sigml', 'r') as file:
            s = socket.socket()
            s.connect(("localhost", 8052))
            data = file.read()
            s.sendall(bytes(data, encoding="utf-8"))
        time.sleep(1)

convert() 
