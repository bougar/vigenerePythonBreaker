#!/usr/bin/python
from crypto import *
from caesar import *
import operator
from fractions import gcd

class vigenereCrack:
    def __init__(self, filename):
        self.text = Text(filename)

    def countOcc(l): # return list with (decimal_char, occ) 
        d={}
        for elt in l:
            if d.has_key(elt):
                d[elt] += 1
            else:
                d[elt] = 1
        return sorted(d.items(),key=lambda x: x[1], reverse=True)


    #Return the number of repeated tuples and divisors of its distances
    #Entrada -> string
    #Salida -> number, lista
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
                freq.extend(self.getDivisors(diff))

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
        a = self.getKeyLen(self.getTuples()) 
        b = self.separeString(a)
        cracker = CaesarCrack()
        for i in range(len(b)):
            cracker.loadFromString(b[i])
            print cracker.crack()
