#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#
# Lars Jørgen Solberg <supersolberg@gmail.com> 2013
#

import argparse, random, os

from wcb import util


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Lists article names')
    parser.add_argument('--number', '-n', type=int)
    parser.add_argument('--randomise', '-r', action='store_true')
    args = parser.parse_args()

    names = util.articles()

    if not args.number:
        args.number = len(names)

    if args.randomise:
        random.shuffle(names)

    for n in names[:args.number]:
        print n.encode('utf-8')
