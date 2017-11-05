#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
    2017 MCPC at UCSY
    Problem-E: Help Decryption
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

    tc.message = list(map(int,sys.stdin.readline().split()))
    tc.m_size = int(sys.stdin.readline())
    tc.matrix = list()
    for i in range(tc.m_size):
        tc.matrix.append(list(map(int,sys.stdin.readline().split())))

    return


def inv_matrix(matrix):
    '''
        matrix: 2D list of number (shall have inverse matrix)
        return: inverse matrix (using sweep method)

        inverse matrix is supported in numpy, you can use it :-)
    '''

    m = matrix[:]   # copy
    m_size = len(m)

    inv = [[1 if r==c else 0 for c in range(m_size)] for r in range(m_size)]

    for row in range(m_size):
        r_pivot = 1/m[row][row]
        for col in range(m_size):
            m[row][col] *= r_pivot
            inv[row][col] *= r_pivot
        for rowx in range(m_size):
            if rowx != row:
                x_mul = m[rowx][row]
                for col in range(m_size):
                    m[rowx][col] -= m[row][col] * x_mul
                    inv[rowx][col] -= inv[row][col] * x_mul

    for row in range(m_size):
        for col in range(m_size):
            inv[row][col] = round(inv[row][col],6)
#            print(inv[row][col], end=' ')
#        print()

    return inv


import string
decode_str = ' ' + string.ascii_lowercase

def decode(message, matrix):
    '''
        message: List of number (size: len(matrix) x n)
        matrix:

        Calculate the product of message and matrix then print
        Return: None
    '''

    m_size = len(matrix)
    for i in range(len(message) // m_size):
        val = [0 for x in range(m_size)]
        for col in range(m_size):
            for pos in range(m_size):  # position in message
#                print ('Val:',val[col], 'msg', message[i*m_size+pos], matrix[pos][col])
                val[col] += message[i*m_size + pos] * matrix[pos][col]

        for x in range(m_size):
            if val[x] < 0 or val[x] > 26:
                print('Unexpected result', val)
                raise ValueError
            print(decode_str[round(val[x])], end = '')

    print()



def solve(tc):
    '''
        Input: Test Case
        Return: None
    '''

    parse_tc(tc)

    inv = inv_matrix(tc.matrix)
    decode(tc.message, inv)

    return


##
##  Main routine
##
if __name__ == '__main__':
    
    tc = TestCase()
    tc.t = int(sys.stdin.readline())
    
    for i in range(tc.t):
        solve(tc)
