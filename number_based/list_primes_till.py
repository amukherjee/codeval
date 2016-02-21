#!/usr/bin/env python -tt
# -*- coding: utf-8 -*-
# Author: Aditya Mukherjee

import sys
import math

def isprime(number):
    """Check to see if the number is prime or not."""

    numnber = abs(int(number))
    if number < 2 : return False
    if number == 2 : return True
    if not number & 1 : return False
    for x in range (3 , int(number**0.5)+1, 2):
        if number % x == 0:
            return False
    return True

def next_prime(number):
    """Finds the next prime number given a starting number."""

    number = number + 1
    while number:
        if isprime(number):
            return number
            break
        number += 1

def list_primes_till(number):
    """Creates a list of primes coma delimited."""

    prime  = 2
    prime_list = []

    while prime < number:
        prime_list.append(',')
        prime_list.append(str(prime))
        prime = next_prime(prime)

    return prime_list

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
    """Gets the file and feeds the numbers into the main method.
       Prints out the resultant list after formatting it.

    """

    list_of_primes = []

    with FileContextManager(file_name) as file:

        for line in file.readlines():
            list_of_primes = list_primes_till(int(line))
            list_of_primes.pop(0)
            formatted_list = ''.join(list_of_primes)
            print formatted_list

if __name__ == "__main__":

    if len(sys.argv) !=2:
        print "usage: python list_primes_till.py filename"
        sys.exit(1)

    filename = sys.argv[1]

    accessfile(filename)

