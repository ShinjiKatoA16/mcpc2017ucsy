#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
    2017 MCPC at UCSY
    Problem-C: Picking Blueberries 
'''
import sys


class TestCase():
    pass


def parse_tc(tc):
    '''
        Input: Test Case
        Update: 
        Return: None
    '''

    tc.n, tc.k = list(map(int,sys.stdin.readline().split()))
    tc.bush = list(map(int,sys.stdin.readline().split()))

    return

def check_calc(i, tc):
    '''
        i: bit map, 1b: bush to take, 0b: bush not to take
        Return: 0 if invalid, accumulated value otherwize
    '''

    acc_val = 0
    idx = 0
    prev_taken = False

#    print('bitmap:', bin(i), end=' ')
    while i > 0:
        bit = i & 1
        if bit:
#            print('prev_taken:', prev_taken, end = ' ')
            if prev_taken:
                prev_taken = False
                i >>= 1  # i //= 2
                idx += 1
                continue
            acc_val += tc.bush[idx]
            prev_taken = True
        else:
            prev_taken = False

        i >>= 1  # i //= 2
        idx += 1

#    print('value:', acc_val)
    return acc_val



def solve(tc):
    '''
        Input: Test Case
        Return: None
    '''

    parse_tc(tc)

    max_berry = 0
    for i in range(tc.n**2-1):
        val = check_calc(i, tc)
        if val <= tc.k and val > max_berry: max_berry = val

    print(max_berry)
    return


##
##  Main routine
##
if __name__ == '__main__':
    
    tc = TestCase()
    tc.t = int(sys.stdin.readline())
    
    for i in range(tc.t):
        solve(tc)
