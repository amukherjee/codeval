#!/usr/bin/env python

import argparse

class gridUtils():

    def __init__(self):
        self.summation = 0

    def digit_sum(self, num):
        if (num / 10) <= 10 :
            self.summation += ( num / 10 ) + ( num % 10 )

        elif (num/10 == 0 ):
            self.summation += 0
            self.digit_sum ( num / 10)

        else :
            self.summation += 1
            self.digit_sum( num / 10 )

        return self.summation


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("number")
    args = parser.parse_args()

    g = gridUtils()

    print g.digit_sum(int(args.number))

