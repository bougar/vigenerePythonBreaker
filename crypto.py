#!/usr/bin/python
from operator import itemgetter

class Text:
    def __init__(self, filename):
        self.load(filename)

    def load(self, filename):
        fp = open(filename, "r")
        self.rawtext = fp.read()
        fp.close()
        self.text = self.convert(self.rawtext)      

    def convert(self, txt):
        rval = ""
        for c in txt.upper():
            if c.isapha():
                rval += c
            return rval

    def __str__(self):
        rval = ""
        pos = 0
        for c in self.text:
            rval += c
            pos += 1
            if pos % 60 == 0:
                rval += '\n'
            elif pos % 5 == 0:
                rval += " "
        return rval

class Freq:
    def __init__(self, txt, n = 1):
        self.count = self.doCount(txt, n)
    
    def doCount(self, txt, n):
        dictionary = {}
        for i in range (n, len(txt)+1):
            s = txt[i-n:i]
            if s in dictionary:
                dictionary[s] += 1
            else:
                dictionary[s] = 1
        return dictionary

    def get(self):
        return self.count

    def __str__(self):
        items = self.count.items()
        items.sort(key=itemgetter(1), reverse=True)
        rval = []
        for i in items:
            rval.append(i.__str__())
         
        return "\n".join(rval)
