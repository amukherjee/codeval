#!/usr/bin/env python2.7 -tt
# -*- coding: utf-8 -*-
# Author: Aditya Mukherjee

import sys

def accessfile(filename):

    data = open(filename).read().splitlines()

    for line in data:
        print line
        categories = line.split(';')
        print categories
        keys = categories.split(':')
        print keys

    pass

#def in_circle(center, radius, point)


if __name__ == "__main__":

    if len(sys.argv) !=2:
        print "usage: python point_in_circle.py input_filename"
        sys.exit(1)

    filename = sys.argv[1]
    accessfile(filename)

