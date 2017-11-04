#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
    2017 MCPC at UCSY
    Problem-G: Concrete Pathway around Pool
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

    tc.l, tc.w = tuple(map(int,sys.stdin.readline().split()))
    tc.a = float(sys.stdin.readline().strip())

    return


def solve(tc):
    '''
        Input: Test Case
        Return: None

        ax^2 + bx + c = 0  --> x = (-b +- sqrt(b^2 - 4ac)) / 2a
        (l+2x)(w+2x)-lw = A  --> 4x^2+2(l+w)x-A = 0
    '''

    parse_tc(tc)
    
    a = 4  # 4x^2
    b = 2*(tc.l+tc.w)
    c = -(tc.a)

    x = (-b + ((b**2 - 4*a*c)**0.5)) / (2*a)  # only positive value

    print(x)
    return


##
##  Main routine
##
if __name__ == '__main__':
    
    tc = TestCase()
    tc.t = int(sys.stdin.readline())
    
    for i in range(tc.t):
        solve(tc)
