#!/usr/bin/python
from crypto import *

class vigenereCrack:
    def __init__(self):
        pass

    #Get divisors of substring distances =D
    @staticmethod
    def getDivisors(n):
        l = []
        for i in range(2,n):
            if n % i == 0:
                l.append(i)
        return l

    @staticmethod
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
    @staticmethod
    def getTuples(string, n = 3):
        freq = []
        distance = {}
        count = 0
        for i in range(len(string)):
            subString = string[i:i+n]
            if ( len(subString) < n ):
                return distance
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
                freq.extend(vigenereCrack.getDivisors(diff))
