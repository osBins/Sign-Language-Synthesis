def sliceSigml():
    with open('SiGML-output.sigml', 'r') as file:
        data = file.read().split("\n")
        data = data[1:-1]

    with open('lol.sigml', 'w') as file:
        for line in data:
            file.write(line)
            file.write("\n")
