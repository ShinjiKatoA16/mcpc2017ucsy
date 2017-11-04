#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
2017 MCPC Rehearsal Problem-A
Query Langueage Interpreter
'''

import sys

def analyze_db(num_db, infile):
    '''
    Read infile whihch contains 'Room Person Object'
    return 4 dictionary:
        room_p: Key Room, Value Person
        room_o: Key Room, Value Object
        person: Key Person, Value Room
        obj:    Key Object, Value Room
    '''

    room_p = dict()
    room_o = dict()
    person = dict()
    obj = dict()

    for i in range(num_db):
        room, psn, ob = infile.readline().split()
        room_p[room] = psn
        room_o[room] = ob 
        person[psn] = room 
        obj[ob] = room 

    return room_p, room_o, person, obj

num_db, num_query = map(int, sys.stdin.readline().split())

room_p, room_o, person, obj = analyze_db(num_db, sys.stdin)

for i in range(num_query):
    query = sys.stdin.readline().split()
    len_q = len(query)

    if len_q == 5 and query[0:4] == ['WHO', 'IS', 'IN', 'THE']:
        finding = query[4][:len(query[4])-1]
        if finding in room_p:
            print(room_p[finding])
        else:
            print('UNKNOWN')
    elif len_q == 5 and query[0:4] == ['WHAT', 'IS', 'IN', 'THE']:
        finding = query[4][:len(query[4])-1]
        if finding in room_o:
            print(room_o[finding])
        else:
            print('UNKNOWN')
    elif len_q == 4 and query[0:3] == ['WHERE', 'IS', 'THE']:
        finding = query[3][:len(query[3])-1]
        if finding in obj:
            print(obj[finding])
        else:
            print('UNKNOWN')
    elif len_q == 3 and query[0:2] == ['WHERE', 'IS']:
        finding = query[2][:len(query[2])-1]
        if finding in person:
            print(person[finding])
        else:
            print('UNKNOWN')
    else:
        print('ERROR')
