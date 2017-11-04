#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
    2017 MCPC at UCSY
    Problem-E: Stacking Plates
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
    tc.stacks = list()

    for i in range(tc.n):
        tc.stacks.append(sys.stdin.readline().split()) # 2D list

    return


def reform_stack(org):
    '''
        Input: tc.stacks
        Output: cosolidated stacks (no prefix, no duplicate)
    '''

    stacks = list()

    for stack in org:
        prev_val = None
        new_stack = list()

        for i in range(1, len(stack)):
            if stack[i] != prev_val:
                new_stack.append(stack[i])
                prev_val = stack[i]

        stacks.append(new_stack)

    return stacks

def dequeue(listx):
    '''
    x: List
    update: x -> x[1:], remove 1st element
    return 1st element and updated list
    '''

    if listx == []: return None, None

    val = listx[0]
    listx = listx[1:]
    return val, listx

def merge2(list1, list2):
    '''
        list1, list2: List of digits
        Return: merged list of 2
    '''
    new_list = list()
    val1, list1 = dequeue(list1)
    val2, list2 = dequeue(list2)

    while not (val1 == None and val2 == None):
        if val1 == None:
            new_list.append(val2)
            val2, list2 = dequeue(list2)
        elif val2 == None or val1 < val2:
            new_list.append(val1)
            val1, list1 = dequeue(list1)
        else:
            new_list.append(val2)
            val2, list2 = dequeue(list2)

    return new_list

def merge(stacks):
    '''
        stacks: 2D List
        Return: 1D sorted List
    '''

    merged_stack = list()

    for stack in stacks:
        merged_stack = merge2(merged_stack, stack)

#    print('Merged stack', merged_stack)
    return merged_stack

def bound_exist(p, n, stacks):
    '''
        p: digit-1
        n: digit-2
        Return: True if p-n combination exists in stacks
                False otherwise
    '''
    for stack in stacks:
        if p in stack and n in stack:
            if stack.index(p) + 1 == stack.index(n):
                return True

    return False


def check_bound(merged_stack, stacks):
    '''
        merged_stack: combined list
        stacks: Input 2D list
        Return: Number of 2 digit combination in stacks
    '''
    num_found = 0

    prev_val = merged_stack[0]
    for i in range(1, len(merged_stack)):
        next_val = merged_stack[i]
        if bound_exist(prev_val, next_val, stacks):
            num_found += 1
            
    return num_found


def solve(tc):
    '''
        Input: Test Case
        Return: None
    '''

    parse_tc(tc)
    stacks = reform_stack(tc.stacks)
#    print(stacks)
    num_merge = len(stacks) - 1  ## Join Stacks
    for stack in stacks:
        num_merge += (len(stack) - 1) * 2  ## Split and Join

    merged_stack = merge(stacks)

    print(num_merge - check_bound(merged_stack, stacks) * 2)
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
