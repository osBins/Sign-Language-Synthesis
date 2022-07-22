import Ham2SIGML
dict = {"name": "",
        "have": "",
        "deaf": "",
        "children": ""}


def convert():
    with open('text.txt') as file:
        data = file.read().split()
    for i in data:
        res = ''.join(r'\u{:04x}'.format(ord(chr)) for chr in dict[i])
        print(res)
        hamList = [res.encode().decode('unicode_escape')]
        print(hamList)
        Ham2SIGML.readInput(hamList)
convert()
