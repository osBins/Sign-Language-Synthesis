import Ham2SIGML
import socket
from dict import dict
import time
# print(dict)

def convert():
    with open('text.txt') as file:
        data = file.read().split()

    for i in data:
        # handling HamNoSys encoding-decoding via Unicode characters
        res = ''.join(r'\u{:04x}'.format(ord(chr)) for chr in dict[i])
        hamList = [res.encode().decode('unicode_escape')]
        Ham2SIGML.readInput(hamList)
        with open('SiGML-output.sigml', 'r') as file:
            # print("output opened")
            s = socket.socket()
            s.connect(("localhost", 8052))
            # print("socket connected")
            data = file.read()
            # print("sending data to socket")
            s.sendall(bytes(data, encoding="utf-8"))
            # print("data sent, now waiting")
        time.sleep(2)
convert() 


## Code to take dictionary from file. TBI - decoding issue.
# d = {}
# with open("dictionary.txt") as f:
#     for line in f:
#        (key, val) = line.split()
#        d[key] = val
#     print(d)
