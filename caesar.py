#!/bin/python
from crypto import *

class Caesar:
    def __init__(self, filename=0):
        if filename:
            self.text = Text(filename)

    def load(self, filename):
        self.text = Text(filename)

    def loadFromString(self, string):
        self.text = Text()
        self.text.loadFromString(string)

    def encrypt(self, shift):
        output = ""
        string = self.text.get()
        for i in range(len(string)):
            output += chr(((ord(string[i]) - 65 + shift) % 26) + 65)
        return output
        
    def decrypt(self, shift):
        output = ""
        string = self.text.get()
        for i in range(len(string)):
            output += chr(((ord(string[i]) - 65 - shift) % 26) + 65)
        return output
        
        
class CaesarCrack:
    def __init__(self, filename=0):
        if filename:
            self.text = Text(filename)

    def load(self, filename):
        self.text = Text(filename)

    def loadFromString(self, string):
        self.text = Text()
        self.text.loadFromString(string)

    def getScore(self, key):
        spanish = [.1253,.0142,.0468,.0586,.1368,.0069,.0101,.0070,
                    .0625,.0044,.0001,.0497,.0315,.0671,.0868,.0251,
                    .0088,.0687,.0798,.0463,.0393,.0090,.0002,.0022,
                    .0090,.0052]
        caesar = Caesar()
        caesar.loadFromString(self.text.get())
        testString = caesar.decrypt(ord(key) - 65)
        return sum(spanish[ord(char) - 65] for char in testString) 
        

    def getPossibleKeys(self,dictionary):
        maximum = 0
        l = []
        char = ''
        for i in range(ord('A'), ord('Z')+1):
            if dictionary.get(chr(i)) is None:
                dictionary[chr(i)] = 0
        for i in range(ord('A'), ord('Z')):
            aux = dictionary[chr(i)] + dictionary[chr(((i - 65 + 4) % 26) + 65 )] + dictionary[chr(((i - 65 + 11) % 26) + 65 )]
            t = chr(i), aux
            l.append(t)
            if aux > maximum:
                maximum = aux
                char = chr(i)
        return sorted(l, key=lambda tup: tup[1], reverse=True)

    def crack(self):
        freq = Freq(self.text.get(), 1).get()
        possibleKeys = self.getPossibleKeys(dict(freq))
        maximun = 0
        for i in range(5):
            
            aux = self.getScore(possibleKeys[i][0])
            if aux > maximun:
                maximun = aux
                key = possibleKeys[i][0]
        return key
