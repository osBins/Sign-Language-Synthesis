import Ham2SIGML

dict = {"name": "",
        "have": "",
        "deaf": "",
        "children": "",
        "hard": "",
        "lock": "", 
        "hat": "",
        "answer": "",
        "foreigner": "",
        "april": "",
        "arrange": ""}



def convert():
    with open('text.txt') as file:
        data = file.read().split()
    for i in data:
        # handling HamNoSys encoding-decoding via Unicode characters
        res = ''.join(r'\u{:04x}'.format(ord(chr)) for chr in dict[i])
        hamList = [res.encode().decode('unicode_escape')]
        Ham2SIGML.readInput(hamList)
convert() 


## Code to take dictionary from file. TBI - decoding issue.
# d = {}
# with open("dictionary.txt") as f:
#     for line in f:
#        (key, val) = line.split()
#        d[key] = val
#     print(d)
