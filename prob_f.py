#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
    2017 MCPC at UCSY
    Problem-F: Product Distribution
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

    tc.m, tc.n = list(map(int,sys.stdin.readline().split()))
    tc.m_supply = list(map(int,sys.stdin.readline().split()))
    tc.n_capa = list(map(int,sys.stdin.readline().split()))
    max_capa = max(tc.n_capa)
    tc.cost = list()
    for i in range(tc.m):
        cost = list(map(int,sys.stdin.readline().split()))
        for k in range(len(cost)):
            tc.cost.append((cost[k], max_capa-tc.n_capa[k], i, k))

    tc.cost.sort()

    return


def solve(tc):
    '''
        Input: Test Case
        Return: None
    '''

    parse_tc(tc)

    total_cost = 0
    distri = [[0 for i in range(tc.n)] for i in range(tc.m)] 

    for c in tc.cost:
        idx_m = c[2]
        idx_n = c[3]
        transport = min(tc.m_supply[idx_m], tc.n_capa[idx_n])
        if transport:
            total_cost += transport * c[0]
            tc.m_supply[idx_m] -= transport
            tc.n_capa[idx_n] -= transport
            distri[idx_m][idx_n] = transport

    for row in range(tc.m):
        for col in range(tc.n):
            if col == tc.n-1: eol = '\n'
            else: eol = ','
            print(distri[row][col], end=eol)

    print(total_cost)

    return


##
##  Main routine
##
if __name__ == '__main__':
    
    tc = TestCase()
    tc.t = int(sys.stdin.readline())
    
    for i in range(tc.t):
        print('Case: ', i+1, ':', sep ='')
        solve(tc)
