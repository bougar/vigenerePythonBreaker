#!/usr/bin/python
from crypto import *
from caesar import *
import operator
from fractions import gcd
import logging

class vigenereCrack:
    def __init__(self, filename):
        self.text = Text(filename)

    def getTuples(self, n = 3):
        string = self.text.get()
        freq = []
        distance = {}
        count = 0
        for i in range(len(string)):
            subString = string[i:i+n]
            if ( len(subString) < n ):
                return (sorted(distance.items(),key=operator.itemgetter(1), reverse=True))
            j = i+1 

            try:
                string.index(subString, j)
                count = count + 1
            except:
                pass

            while (j + n < len(string) ):
                try:
                    d = string.index(subString, j)
                except:
                    break
                diff = d - i
                try:
                    distance[diff] = distance[diff] + 1
                except:
                    distance[diff] = 1
                j += len(subString) + d

    def getKeyLen(self, distanceList, n = 5):
        subList = distanceList[0:n]
        a = [[x[0] for x in subList]]
        a = a[0]
        b = a[0]
        for i in range(1,len(a)):
            b = gcd(a[i], b)
        return b

    def separeString(self, keyLength):
        l = []
        for  i in range(keyLength):
            if i > len(self.text.get()):
                break
            l.append("")
            for j in range( i, len(self.text.get()), keyLength ):
                if j > len(self.text.get()):
                    break
                l[i] += self.text.get()[j]
        return l
                
    def crack(self):
        if ( len(self.text.get()) < 500 ):
            loggin.warning("Text is so small")
        a = self.getKeyLen(self.getTuples()) 
        b = self.separeString(a)
        cracker = CaesarCrack()
        key = ""
        for i in range(len(b)):
            cracker.loadFromString(b[i])
            key += cracker.crack()
        return key 
