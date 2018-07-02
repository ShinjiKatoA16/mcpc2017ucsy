#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
    2017 MCPC at UCSY
    Problem-G: Concrete Pathway around Pool (Binary Search version)
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

    tc.l, tc.w = map(float,sys.stdin.readline().split())
    tc.a = float(sys.stdin.readline().strip())

    return


def search_lowhigh(tc, low, high):
    low_area = (tc.w + low*2) * (tc.l + low*2) - (tc.w * tc.l)
    high_area = (tc.w + high*2) * (tc.l + high*2) - (tc.w * tc.l)
    if low_area <= tc.a and high_area >= tc.a:
        return low, high
    elif high_area < tc.a:
        return search_lowhigh(tc, high, high*2)
    else:
        raise 'Logic error'


def bsearch(tc, low, high):
    mid = (low+high) / 2
    area = (tc.w + mid*2) * (tc.l + mid*2) - (tc.w * tc.l)

    if area < tc.a:
        if high-mid <= 0.001:
            return (high+mid) / 2
        else:
            return bsearch(tc, mid, high)
    else:
        if mid-low <= 0.001:
            return (mid+low) / 2
        else:
            return bsearch(tc, low, mid)

def solve(tc):
    '''
        Input: Test Case
        Return: None
    '''

    parse_tc(tc)
    
    low, high = search_lowhigh(tc, 0, 1)

    x = bsearch(tc, low, high)
    
    print(round(x,2))
    return


##
##  Main routine
##
if __name__ == '__main__':
    
    tc = TestCase()
    tc.t = int(sys.stdin.readline())
    
    for i in range(tc.t):
        solve(tc)
