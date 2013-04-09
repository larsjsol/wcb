#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#
# Lars Jørgen Solberg <supersolberg@gmail.com> 2013
#

import os
import argparse

from wcb import util
from wcb import srilm

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('lm_dir')
    parser.add_argument('clean_set')
    parser.add_argument('dirty_set')
    args = parser.parse_args()

    print "classifier\tppl_clean\tppl_dirty\tavg"
    for classifier in util.classifiers(args.lm_dir):
        ppl_clean = srilm.perplexity(os.path.join(args.lm_dir, classifier[1]), args.clean_set, classifier[3])[0]
        ppl_dirty = srilm.perplexity(os.path.join(args.lm_dir, classifier[2]), args.dirty_set, classifier[3])[0]
        print "{0}\t{1:.4f}\t{2:.4f}\t{3:.4f}".format(classifier[0], ppl_clean, ppl_dirty, (ppl_clean + ppl_dirty) / 2)
