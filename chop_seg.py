#!/usr/bin/env python
# -*- coding: utf-8 -*-
#===============================================================================
#
# Copyright (c) 2017 <stakeholder> All Rights Reserved
#
#
# File: /Users/hain/ai/chop-evaluate/chop_seg.py
# Author: Hai Liang Wang
# Date: 2017-07-20:13:20:10
#
#===============================================================================

"""
   TODO: Module comments at here
   
   
"""

__copyright__ = "Copyright (c) 2017 . All Rights Reserved"
__author__    = "Hai Liang Wang"
__date__      = "2017-07-20:13:20:10"


import os
import sys
curdir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(curdir)

from tqdm import trange
import chop

from chop.hmm import Tokenizer as HMMTokenizer
from chop.mmseg import Tokenizer as MMSEGTokenizer

HT = HMMTokenizer()
MT = MMSEGTokenizer()

def evaluate(tokenizer, input, output):
    output_lines = []
    input_lines = []
    with open(input, 'r') as f:
        for x in f.readlines():
            input_lines.append(x)
    
    for x in trange(len(input_lines)):
        # print("seg: %s" % input_lines[x])
        o = []
        for y in tokenizer.cut(input_lines[x]):
            if y.strip(): o.append(y.strip())
        output_lines.append(' '.join(o) + '\n')
        
    print("done.")

    with open(output, 'w') as fr:
        fr.writelines(output_lines)

def main():
    evaluate(HT, 'icwb2-data/testing/msr_test.utf8', 'result/chop.hmm.msr_test.utf8')
    evaluate(MT, 'icwb2-data/testing/msr_test.utf8', 'result/chop.mmseg.msr_test.utf8')

if __name__ == '__main__':
    main()
