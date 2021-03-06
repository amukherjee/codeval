#!/usr/bin/env python -tt
# -*- coding: utf-8 -*-
# Author: Aditya Mukherjee
#import  argparse, math
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

def next_prime( number):
    """Finds the next prime number given a starting number."""

    number = number + 1
    while number:
        if isprime(number):
            return number
            break
        number += 1

def sum_of_first_primes(limit):
    """Returns the sum of first primes up to input number. """

    sum_ = 0
    number = 2
    counter = 0
    while counter < limit:
        if isprime(number):
            sum_ += number
            counter += 1
            number = next_prime(number)
            #print " counter",counter , " prime",number , " sum = ",sum_
    return sum_


if __name__ == "__main__":
    print sum_of_first_primes(1000)
#    parser = argparse.ArgumentParser()
#    parser.add_argument("number")
#    args = parser.parse_args()
#
#
#    sum_of_first_primes(int(args.number))

