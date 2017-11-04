#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
    2017 MCPC at UCSY
    Problem-B: Selfie Selfie Star 
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

    tc.name, tc.num = sys.stdin.readline().split()
    tc.num = int(tc.num)
    tc.fn_m, tc.fn_b = list(map(float,sys.stdin.readline().split()))
    tc.vertex = list()
    for i in range(tc.num):
        tc.vertex.append(list(map(float,sys.stdin.readline().split())))

    return


def calc_intercept(x, y, m):
    '''
        x, y: coordinate
        m: slope

        return b:
        y = mx + b
        b = y - mx
    '''

    return y - m*x

def reflect(x, y, f_m, f_b):
    '''
        x, y: float, coordinate
        f_m: float, slope
        f_b: y intersection point
    '''

    if x*f_m + f_b == y:  # x,y is on the primary funtion
        return x,y

    m0 = -1/f_m   # slope of orthogonal function, slope f_m . m0 => 90deg
    b0 = calc_intercept(x, y, m0)
#    print('y intercept:', x, y, m0, b0)

    # y = f_m * x  + f_b
    # y = m0 * x + b0
    # (f_m - m0) * x + (f_b - b0) = 0   x: cross point
    # (f_m - m0) * x = - (f_b - b0) = (b0 - f_b)
    cross_x = (b0 - f_b) / (f_m - m0)
    cross_y = cross_x * f_m + f_b

    diff_x = x - cross_x
    diff_y = y - cross_y
#    print('Cross:', cross_x, cross_y, diff_x, diff_y)

    return x-(diff_x * 2), y-(diff_y * 2)
    

def solve(tc):
    '''
        Input: Test Case
        Return: None
    '''

    parse_tc(tc)
    print(tc.name, tc.num)

    for v in tc.vertex:
        if tc.fn_m == 0:   # y = b
            x = v[0]
            y = v[1] - (v[1]-tc.fn_b)*2
        else:
            x,y = reflect(v[0], v[1], tc.fn_m, tc.fn_b)
        print(round(x,6), round(y,6))

    return


##
##  Main routine
##
if __name__ == '__main__':
    
    tc = TestCase()
    tc.t = int(sys.stdin.readline())
    
    for i in range(tc.t):
        solve(tc)
