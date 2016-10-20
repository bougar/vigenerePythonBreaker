#!/bin/bash
from crypto import *
class Vigenere:
    
    def __init__(self,filename=0):
        if filename:
            self.text = Text(filename)

    def load(self, filename):
        self.text = Text(filename)

    def loadFromString(self, string):
        self.text = Text()
        self.text.loadFromString(string)

    def cipher(self, key):
        rawText = self.text.getRawText()
        res = ""
        j = 0
        for i in range(len(rawText)):
            if (rawText[i] >= 'A' and rawText[i] <= 'Z'):
                res += chr(((ord(rawText[i]) - 65 + ord(key[j%len(key)]) - 65) % 26) + 65) 
                j += 1
            else:
                res += rawText[i]
        return res

    def decipher(self, key):
        rawText = self.text.getRawText()
        res = ""
        j = 0
        for i in range(len(rawText)):
            if (rawText[i] >= 'A' and rawText[i] <= 'Z'):
                res += chr(((ord(rawText[i]) - 65 - ord(key[j%len(key)]) - 65) % 26) + 65) 
                j += 1
            else:
                res += rawText[i]
        return res
