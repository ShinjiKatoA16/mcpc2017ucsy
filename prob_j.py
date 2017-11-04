#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
    2017 MCPC at UCSY
    Problem-J: Number Conversion
'''
import sys

table3 = ((3000, 'MMM'), (2000, 'MM'), (1000, 'M'))

table2 = ((900, 'CM'), (400, 'CD'), (800, 'DCCC'), (700, 'DCC'), (600, 'DC'), \
         (500, 'D'), (300, 'CCC'), (200, 'CC'), (100, 'C'))

table1 = ((90, 'XC'), (40, 'XL'), (80, 'LXXX'), (70, 'LXX'), (60, 'LX'), \
         (50, 'L'), (30, 'XXX'), (20, 'XX'), (10, 'X'))

table0 = ((9, 'IX'), (4, 'IV'), (8, 'VIII'), (7, 'VII'), (6, 'VI'), \
         (5, 'V'), (3, 'III'), (2, 'II'), (1, 'I'))

all_table = table3 + table2 + table1 + table0


class TestCase():
    pass


def parse_tc(tc):
    '''
        Input: Test Case
        Update: 
        Return: None
    '''

    query = sys.stdin.readline().split()

    tc.convert = query[0] # 'R' or 'D'
    tc.num = int(query[1])
    tc.f_val = list()
    for i in range(tc.num):
        if tc.convert == 'D':  # Decimal to Roman
            tc.f_val.append(int(query[2+i]))
        else:
            tc.f_val.append(query[2+i])

    return

def lookup_roman(val, lookup_table):
    for table in lookup_table:
        if table[0] == val:
            return table[1]

    raise 'Table error'

def to_roman(val):
    '''
        val: integer < 4000
    '''

    if val > 4000: raise ValueError

    roman = ''

    digit = (val // 1000) * 1000
    if digit:
        roman += lookup_roman(digit, table3)
        val -= digit

    digit = (val // 100) * 100
    if digit:
        roman += lookup_roman(digit, table2)
        val -= digit

    digit = (val // 10) * 10
    if digit:
        roman += lookup_roman(digit, table1)
        val -= digit

    digit = val % 10
    if digit:
        roman += lookup_roman(digit, table0)

    return roman


def to_decimal(roman):

    val = 0

    while roman != '':
        for tbl in all_table:
            if tbl[1] == roman[0:len(tbl[1])]:
                val += tbl[0]
                roman = roman[len(tbl[1]):]
                break
        else:
            raise 'Table error (from Roman)'

    return val

def solve(tc):
    '''
        Input: Test Case
        Return: None
    '''

    parse_tc(tc)

    for i in range(tc.num):
        if i == tc.num - 1:
            eol = '\n'
        else: eol = ' '

        if tc.convert == 'D':
            print(to_roman(tc.f_val[i]), end=eol)
        else:
            print(to_decimal(tc.f_val[i]), end=eol)

    return


##
##  Main routine
##
if __name__ == '__main__':
    
    tc = TestCase()
    tc.t = int(sys.stdin.readline())
    
    for i in range(tc.t):
        solve(tc)
