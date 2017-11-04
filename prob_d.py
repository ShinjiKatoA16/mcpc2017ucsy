#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
    2017 MCPC at UCSY
    Problem-D: Car showroom
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

    tc.size = int(sys.stdin.readline())
    tc.n = int(sys.stdin.readline())
    tc.car = sys.stdin.readline().split()

    return


def set_car(car, room, room_size):
    '''
        car: String representing Car number
        room: showroom (List)
        room_size: max length of the room
        Return True if car placement is required
               False if car is already in the room
    '''
    if car in room:
        room.remove(car)
        room.append(car)
        return False

    if len(room) < room_size:
        room.append(car)
        return True

    # Remove LRU(top of list), and add new car to bottom of list
    room.pop(0)
    room.append(car)
    return True

def solve(tc):
    '''
        Input: Test Case
        Return: None
    '''

    parse_tc(tc)

    room = list()
    place_count = 0

    for i in range(tc.n):
#        print(tc.n, tc.car[i], room)
        if set_car(tc.car[i], room, tc.size):
            place_count += 1

    print(place_count)
    return


##
##  Main routine
##
if __name__ == '__main__':
    
    tc = TestCase()
    tc.t = int(sys.stdin.readline())
    
    for i in range(tc.t):
        solve(tc)
