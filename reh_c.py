#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
    2017 MCPC at UCSY
    Problem-C: Secret Chamber at Mount Rushmore
'''
import sys


class TestCase():
    pass


def extend_tr(tr_dict):
    '''
    extend trans_dict. if a->b and b->c, add a->c
    return True: if dictionary is updated
           False: otherwise
    '''

    updated = False
    for f_char in tr_dict:
        for t_char in tr_dict[f_char]:  # tr_dict[f_char]: list
            if t_char in tr_dict:
                for c in tr_dict[t_char]:
                    if c not in tr_dict[f_char] and c != f_char:
                        tr_dict[f_char].append(c)
                        updated = True

    return updated


def parse_tc(tc):
    '''
        Input: Test Case
        Update: 
        Return: Dictionary, key: from-char, value: list of to-char
    '''

    tc.m, tc.n = tuple(map(int,sys.stdin.readline().split()))
    trans_dict = dict()
    tc.query = list()

    for i in range(tc.m):
        f, t = sys.stdin.readline().split()
        if f in trans_dict:
            trans_dict[f].append(t)
        else:
            trans_dict[f] = [t]

    for i in range(tc.n):
        f, t = sys.stdin.readline().split()
        tc.query.append((f,t))


    while extend_tr(trans_dict): pass

    return trans_dict

def is_match(f_str, t_str, tr_dict):
    '''
    f_str: String
    t_str: String
    tr_dict: Dictionary

    return: True if f_str can be converted to t_str
            False otherwise
    '''
    if len(f_str) != len(t_str): return False

    for i in range(len(f_str)):
        c = f_str[i]
        if c != t_str[i]:
            if c not in tr_dict: return False
            for x in tr_dict[c]:
                if x == t_str[i]: break
            else: # not found in dictionary
                return False

    return True

def solve(tc):
    '''
        Input: Test Case
        Return: None
    '''

    trans_dict = parse_tc(tc)

    for f_str, t_str in tc.query:
        if is_match(f_str, t_str, trans_dict):
            print('yes')
        else: print('no')

    return


##
##  Main routine
##
if __name__ == '__main__':
    
    tc = TestCase()
    
    solve(tc)
