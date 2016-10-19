#!/bin/python
from crypto import *
class CaesarCrack:
    def __init__(self, filename=0):
        if filename:
            self.text = Text(filename)

    def load(self, filename):
        self.text = Text(filename)

    def loadFromString(self, string):
        self.text = Text()
        self.text.loadFromString(string)

    def SpyCoder(self, S, N):
        y = ""
        for i in S:
            if(i.isupper()):
                x = ord(i)
                x += N
                if x > ord('Z'):
                    x -= 26
                elif x < ord('A'):
                    x += 26
            y += chr(x)
        return y

    def getKey(self,dictionary):
        maximum = 0
        char = ''
        for i in range(ord('A'), ord('Z')+1):
            if dictionary.get(chr(i)) is None:
                dictionary[chr(i)] = 0
        for i in range(ord('A'), ord('Z')):
            aux = dictionary[chr(i)] + dictionary[chr(((i - 65 + 4) % 26) + 65 )] + dictionary[chr(((i - 65 + 11) % 26) + 65 )]
            if aux > maximum:
                maximum = aux
                char = chr(i)
        return char

    def crack(self):
        freq = Freq(self.text.get(), 1).get()
        a = [[x[0] for x in freq]]
        a = a[0]
        b = a[0]
        key1 = chr ( ( (ord(a[0]) - ord('E') ) % 26) + 65 )
        key2 = chr ( ( (ord(a[0]) - ord('A') ) % 26) + 65 )
        
        return self.getKey(dict(freq))
