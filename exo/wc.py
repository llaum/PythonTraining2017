#!/usr/bin/env python3
# Exercice: recode wc en python
# > python wc.py fichier.txt
from sys import argv
from os.path import exists


def counting(filename):
    """ Counts lines, characters & words """
    nLines = nWords = nChars = 0
    with open(filename, 'r') as f:
        for line in f:
            nLines += 1
            nChars += len(line)
            nWords += len(line.split())
    return nLines, nWords, nChars


if len(argv) < 2:
    print("Not enough arguments!")
    exit(1)
else:
    for filename in argv[1:]:
        if exists(filename):
            print("%d lines, %d words, %d chars" % counting(filename), "in file", filename)
        else:
            print("File not found:", filename)
    exit(0)
