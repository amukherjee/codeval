#!/usr/bin/env python -tt
# -*- coding: utf-8 -*-
# Author: Aditya Mukherjee
#import  argparse, math
import math


def isprime(number):
    """Check to see if the number is prime or not."""

    number = abs(int(number))
    if number < 2 : return False
    if number == 2 : return True
    if not number & 1 : return False
    for x in range (3 , int(number**0.5)+1, 2):
        if number % x == 0:
            return False
    return True

def next_prime(number):
    """Finds the next prime number given a starting number."""

    while number >= 2 :
        if isprime(number):
            return number
            break
        number -= 1

def reverse_number(number, partial=0):
    """Returns the reverse of number."""

    if number == 0 :
        return partial
    return reverse_number( number/10 , partial * 10 + number % 10)

def largest_prime_palindrome(limit):
    """Returns the largest prime palindrome given a limit."""

    counter = limit
    while counter >= 2:
        if isprime(counter):
            if reverse_number(counter) == counter:
                return counter
            counter = next_prime(counter)
        counter = counter - 1

if __name__ == "__main__":
    print largest_prime_palindrome(1000)
