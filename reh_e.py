#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
    2017 MCPC at UCSY
    Problem-E: Stacking Plates
'''
import sys


class TestCase():
    pass


class Plates():
    # Groupt of same radius plates in merged stack
    # id_list: list of stack ID
    def __init__(self, radius, id_list):
        self.radius = radius
        self.id_list = id_list
        self.top = None
        self.bottom = None

    def match_prev(self, prev_bottom):
        self.top = list()
        for stack_id in self.id_list:
            if stack_id in prev_bottom:
                self.top.append(stack_id)
        self.bottom = self.id_list.copy()
        if len(self.top) == 1 and len(self.bottom) != 1:
            self.bottom.remove(self.top[0])

        return

    def __repr__(self):
        return ('Plates {}: {}, top: {} bottom: {}'.format(self.radius, self.id_list, self.top, self.bottom))


def parse_tc(tc):
    '''
        Input: Test Case
        Update: 
        Return: None
    '''

    tc.n = int(sys.stdin.readline())
    tc.stacks = list()

    for i in range(tc.n):
        stack = sys.stdin.readline().split()[1:]  # 2d List, 1st=len
        tc.stacks.append(stack)

    return


def reform_stack(org):
    '''
        Input: tc.stacks
        Output: cosolidated stacks (no prefix, no duplicate)
    '''

    stacks = list()
    stack_id = 0

    for stack in org:
        prev_radius = None
        new_stack = list()

        for radius in stack:
            if radius != prev_radius:
                new_stack.append((radius, stack_id))
            prev_radius = radius

        stacks.append(new_stack)
        stack_id += 1

    return stacks


def merge(stacks):
    '''
        stacks: 2D List of tuple(radius, id)
        Return: 1D sorted List
    '''

    merged_stack = list()

    for stack in stacks:
        merged_stack.extend(stack)

    merged_stack.sort()

    return merged_stack


def stack2plates(merged_stack):
    '''
    merged_stack: List of Tuple(radius, id)
    return: List of Plates
    '''

    plates_list = list()
    id_list = list()
    prev_size = None

    for plate in merged_stack:
        radius, plate_id = plate
        if radius != prev_size:
            if id_list:
                plates_list.append(Plates(prev_size, id_list))
            id_list = [plate_id]
        else:
            id_list.append(plate_id)

        prev_size = radius

    if id_list:
        plates_list.append(Plates(radius, id_list))

    return plates_list


def max_reuse(plates_list):

    reuse = 0
    prev_bottom = list()

    for plates in plates_list:
        plates.match_prev(prev_bottom)
        if plates.top: reuse += 1
        prev_bottom = plates.bottom
        #print(plates, file=sys.stderr)

    return reuse

def solve(tc):
    '''
        Input: Test Case
        Return: Numper of movement
    '''

    parse_tc(tc)
    stacks = reform_stack(tc.stacks)
    #print(stacks)
    num_merge = len(stacks) - 1  ## Join Stacks
    for stack in stacks:
        num_merge += (len(stack) - 1) * 2  ## Split and Join

    merged_stack = merge(stacks)
    plates_list = stack2plates(merged_stack)  # list of Plates

    #return (num_merge - check_bound(merged_stack, stack_bound) * 2)
    return (num_merge - max_reuse(plates_list) * 2)


##
##  Main routine
##
if __name__ == '__main__':
    
    tc = TestCase()
    tc.t = int(sys.stdin.readline())
    
    for i in range(tc.t):
        print('Case {}:{}'.format(i+1, solve(tc)))
