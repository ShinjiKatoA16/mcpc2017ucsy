#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
    2017 MCPC at UCSY
    Problem-I: Money Drop Game

    The description of this problem is not clear, and may be there are
    mistakes in the description or sample input/output.

    Assumes that the number of bundles to 20 (50 in description)
'''

NUM_BUNDLE = 20
KYAT_PER_BUNDLE = 500000

import sys


class TestCase():
    pass


def parse_tc(tc):
    '''
        Input: Test Case
        Update: 
        Return: None
    '''

    tc.n = int(sys.stdin.readline())
    tc.quiz = list()
    for i in range(tc.n):
        tc.quiz.append(sys.stdin.readline().split())

    return


def solve(tc):
    '''
        Input: Test Case
        Return: None
    '''

    parse_tc(tc)

    print(total)
    return


##
##  Main routine
##
if __name__ == '__main__':
    
    tc = TestCase()
    tc.t = int(sys.stdin.readline())
    
    for i in range(tc.t):
        print('Case ', i+1, ':', sep='', end='')
        solve(tc)
