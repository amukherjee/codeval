#!/usr/bin/env python -tt
# -*- coding: utf-8 -*-
# Author: Aditya Mukherjee

from sys import argv
from sys import exit


class FileContextManager():

    def __init__(self,file_name):
        self._file_name = file_name
        self._file = None

    def __enter__(self):
        self._file = open(self._file_name)
        return self._file

    def __exit__(self,cls, value, tb):
        self._file.close()

def accessfile(filename):

    with FileContextManager(filename) as file:
        for line in file.readlines():
            print count_ones(int(line))
    pass

def count_ones(line):

    binary = bin(line)
    string = str(binary)
    total_ones = string.count('1')

    return total_ones

if __name__ == "__main__":

    if len(argv) !=2:
        print "usage: python count_1s.py filename"
        exit(1)

    filename = argv[1]

    accessfile(filename)
