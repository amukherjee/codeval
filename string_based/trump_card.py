#!/usr/bin/env python -tt
# -*- coding: utf-8 -*-
# Author : Aditya Mukherjee

import sys

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
    """Files are accessed form here. """
    with FileContextManager(file_name) as file:
        for line in file.readlines():
            winner = evaluate_winner(line)
            print ' '.join(winner)
    pass

def evaluate_winner(line):
    """ Constraints for  winning are set here."""

    trump = line.split('|')[1]
    candidates = line.split('|')[0]

    first = candidates.split(' ')[0]
    second = candidates.split(' ')[1]

    value_first = evaluate_value(first, trump.strip())
    value_second = evaluate_value(second, trump.strip())

    winner =[]

    if value_first > value_second:
        winner.append(first)
    elif value_first < value_second:
        winner.append(second)
    else:
        winner.append(first)
        winner.append(second)

    return winner

def evaluate_value(candidate, trump):
    """Trump and Simple card values are quantified here."""

    rank = candidate[:-1]
    is_trump = candidate[-1:]

    if ( is_trump == trump ):
        value = 100
    elif rank == 'A':
        value = 14
    elif rank == 'K':
        value = 13
    elif rank == 'Q':
        value = 12
    elif rank == 'J':
        value = 11
    else:
        value = int(rank)

    return value

def main():
    if len(sys.argv) != 2:
        print "usage: ./trump_card.py filename"
        sys.exit(1)

    filename = sys.argv[1]

    accessfile(filename)

if __name__ == '__main__':
    main()
