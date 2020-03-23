import pickle

FILENAME = 'file.pickle'

s = open('dumped.txt', 'a+')

with open(FILENAME, "rb") as file:
    addresses = pickle.load(file)
    for i in addresses:
        s.write(i + '\n')

