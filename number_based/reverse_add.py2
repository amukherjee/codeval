#!/usr/bin/env python -tt
# -*- coding: utf-8 -*-
# Author: Aditya Mukherjee

from sys import argv as argv
from sys import exit as exit

class FileContextManager():
    def __init__(self,file_name):
        self._file_name = file_name
        self._file = None

    def __enter__(self):
        self._file = open(self._file_name)
        return self._file

    def __exit__(self,cls, value, tb):
        self._file.close()

def accessfile(file_name):
    with FileContextManager(file_name) as file:
        for line in file.readlines():
            find_palindrome(int(line))
    pass

def find_palindrome(number):
    """ Finding the Palindrome."""
    sum_ = number
    reverse_number = 0
    count = 0
    while not is_palindrome(sum_):
        reverse_number = get_reverse_number(sum_)
        sum_ +=  reverse_number
        count += 1

    print count, sum_

def get_reverse_number(number):
    """ Getting the reverse of a number."""
    numb_str = str(number)
    reverse = numb_str[::-1]

    return int(reverse)

def is_palindrome(number):
    """ Testing number for palindrome syndrome."""
    numb_str = str(number)

    return numb_str == numb_str[::-1]

def main():
    if len(argv) != 2:
        print "usage: ./reverse_add.py filename"
        exit(1)

    filename = argv[1]

    accessfile(filename)

if __name__ == '__main__':
    main()
