#!/usr/bin/python

import sys
from optparse import OptionParser
import vigenere 
import kasisky
def doBreak(fromFile, toFile = 0):
    k = kasisky.vigenereCrack(fromFile)
    v = vigenere.Vigenere(fromFile)
    key = k.crack()
    print "Obtained key: " + key + "\n"
    if toFile:
        f = open(toFile, 'w+')
        f.write(v.decipher(key))
        f.close()
    else:
        print (v.decipher(key))
        
def encrypt(fromFile, key, toFile = 0):
    v = vigenere.Vigenere(fromFile)
    c = v.cipher(key)
    if (toFile):
        f = open(toFile, 'w+')
        f.write(c)
        f.close()
    else:
        print c

def decrypt(fromFile, key, toFile = 0):
    v = vigenere.Vigenere(fromFile)
    c = v.decipher(key)
    if (toFile):
        f = open(toFile, 'w+')
        f.write(c)
        f.close()
    else:
        print c
    
def main():

    parser = OptionParser()
    parser.add_option("-e", "--encrypt", action="store_true", dest="encrypt")
    parser.add_option("-d", "--decrypt", action="store_true", dest="decrypt")
    parser.add_option("-b", "--break", action="store_true", dest="doBreak")
    parser.add_option("-k", "--keyword", dest="keyword")
    parser.add_option("-o", "--output", dest="outputFilename") 
    parser.add_option("-i", "--input", dest="inputFilename") 

    (options, args) = parser.parse_args()

    if (options.encrypt and options.decrypt or 
    options.encrypt and options.doBreak or 
    options.decrypt and options.doBreak):
        print "Encrypt, decrypt and break are mutually exclusive"
        sys.exit(1)
           
    if not options.encrypt and not options.decrypt and not options.doBreak:
        options.encrypt = True # encrypt is default

    if ((options.encrypt or options.decrypt) and
            ((not options.keyword) or (not options.inputFilename))):
        print "Must set keywords and input file name if encrypt or decrypt"
        sys.exit(1)

    if (options.doBreak and
            (options.keyword)):
        print "Cannot set keywords if break"
        sys.exit(1)

    if (options.doBreak and
            (not options.inputFilename)):
        print "Must set input file name to break"

    if options.encrypt:
        encrypt(options.inputFilename, options.keyword, options.outputFilename)
    elif options.decrypt:
        decrypt(options.inputFilename, options.keyword, options.outputFilename)
    elif options.doBreak:
        doBreak(options.inputFilename, options.outputFilename)

if __name__ == "__main__":
    main()
