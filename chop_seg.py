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

T = chop.Tokenizer(dict_path=os.path.join(chop.__path__[0], 'dict.txt'))


def evaluate(input, output):
    output_lines = []
    input_lines = []
    with open(input, 'r') as f:
        for x in f.readlines():
            input_lines.append(x)
    
    for x in trange(len(input_lines)):
        print("seg: %s" % input_lines[x])
        output_lines.append(' '.join(T.cut(input_lines[x])) + '\n')
        print("done.")

    with open(output, 'w') as fr:
        fr.writelines(output_lines)

def main():
    evaluate('icwb2-data/testing/pku_test.utf8', 'result/chop.pku_test.utf8')

if __name__ == '__main__':
    main()
