#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
    2017 MCPC at UCSY
    Problem-H: Counting Vertex
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

    tc.n = int(sys.stdin.readline())
    tc.vertex = list()

    for i in range(tc.n):
        x,y = list(map(int,sys.stdin.readline().split()))
        tc.vertex.append([y, x, None])

    return


def set_intersection(tc):
    for i in range(tc.n):
        if i == 0:
            prev_v = tc.vertex[tc.n-1]
        else:
            prev_v = tc.vertex[i-1]

        if i == tc.n - 1:
            next_v = tc.vertex[0]
        else:
            next_v = tc.vertex[i+1]

        if prev_v[0] > tc.vertex[i][0] and next_v[0] > tc.vertex[i][0]:
            tc.vertex[i][2] = 2
        elif prev_v[0] < tc.vertex[i][0] and next_v[0] < tc.vertex[i][0]:
            tc.vertex[i][2] = 2
        else:
            tc.vertex[i][2] = 1


def solve(tc):
    '''
        Input: Test Case
        Return: None
    '''

    parse_tc(tc)
    set_intersection(tc)
#    tc.vertex.sort(reverse=True)

    for i in range(tc.n):
        if i == tc.n-1:
            eol = '\n'
        else:
            eol = ' '
        print(tc.vertex[i][2], end=eol)

    return


##
##  Main routine
##
if __name__ == '__main__':
    
    tc = TestCase()
    tc.t = int(sys.stdin.readline())
    
    for i in range(tc.t):
        print('Case ', i+1, ':', sep='')
        solve(tc)
