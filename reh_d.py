#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
    2017 MCPC at UCSY
    Problem-?: 
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

    tc.n, tc.k = tuple(map(int,sys.stdin.readline().split()))
    tc.num2d = list()
    for i in range(tc.n):
        nums = tuple(map(int, sys.stdin.readline().split()))
        tc.num2d.append(nums)

    return

class BinTreeNode():
    def __init__(self, val):
        self.val = val
        self.parent = None
        self.left = None
        self.right = None

    def add_left(self, left):
        left.parent = self
        self.left = left

    def add_right(self, right):
        right.parent = self
        self.right = right

    def add_child(self, child):
        if child.val < self.val:
            if self.left == None:
                self.add_left(child)
            else:
                self.left.add_child(child)
        else:
            if self.right == None:
                self.add_right(child)
            else:
                self.right.add_child(child)

    def add_shape(self, shape):
        shape.append((self.parent != None, self.left != None, self.right != None))
        if self.left != None:
            self.left.add_shape(shape)
        if self.right != None:
            self.right.add_shape(shape)


def shape_of_nums(nums):
    '''
    nums: tuple of integers
    return: list of [(True, False, False), ...] of binary tree
    '''

    root = BinTreeNode(nums[0])
    for i in range(1, len(nums)):
        node = BinTreeNode(nums[i])
        root.add_child(node)

    shape = list()
    root.add_shape(shape)
#   print(shape)
    return shape

def solve(tc):
    '''
        Input: Test Case
        Return: None
    '''

    parse_tc(tc)

    x = list()
    for nums in tc.num2d:
        shape = shape_of_nums(nums)
        if shape not in x:
            x.append(shape)

    print(len(x))
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
