#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
    2017 MCPC Rehearsal at UCSY
    Problem-B: Find A Word
'''
import sys


class TestCase():
    pass


def parse_tc(tc):
    '''
        Input: Test Case
        Update: tc.num: number of query  tc.query: word to be found
        Return: None
    '''

    tc.num = int(sys.stdin.readline())
    tc.query = list()
    for i in range(tc.num):
        tc.query.append(sys.stdin.readline().strip())  # remove \n

    return

# matrix: add space before and after, to avoid range check
matrix = ('                      ',
          ' B                  S ',
          ' A FOOTBALL         C ',
          ' SCOBOL  T          I ',
          ' E M    I           E ',
          ' B     D            N ',
          ' A    E             C ',
          ' L   -R             E ',
          ' L  K E  C            ',
          '   N  T O             ',
          '  I   UM              ',
          ' LACSAP               ',
          '     IM               ',
          '    L O               ',
          '   E  C               ',
          '  R                   ',
          '                      ')

def parse_matrix():
    '''
    Input: matrix
    Output: Dictionary key: Character, value: List of coordinate
    '''

    c_dict = dict()

    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            c = matrix[row][col]
            if c != ' ':
                if c in c_dict:
                    c_dict[c].append((row,col))
                else:
                    c_dict[c] = [(row,col)]

#    print(c_dict)
    return c_dict

def find_word(word, char_dict):
    '''
    Input: word, dictionary
    Output: None if not found
            List of coordinate of the word if word is found
    '''

    direction = ((1,0), (1,1), (0,1), (-1,1), (-1,0), (-1,-1), (0,-1), (1,-1))

    first_char = word[0]
    if first_char not in char_dict:
        return None

    for row, col in char_dict[first_char]:
        for dir in direction:
            r_temp, c_temp = row, col
            pos_list = list()
            for c in word:
                if matrix[r_temp][c_temp] != c:
                    break
                pos_list.append((r_temp, c_temp))
                if len(pos_list) == len(word): # found the word
                    return pos_list
                r_temp += dir[0]
                c_temp += dir[1]

    return None

def solve(tc):
    '''
        Input: Test Case
        Return: None
    '''

    parse_tc(tc)

    char_dict = parse_matrix()

    for i in range(tc.num):
        coord = find_word(tc.query[i], char_dict)
        if coord == None:
            print('NOT FOUND')
        else:
            len_word = len(coord)
            for i in range(len_word):
                if i == len_word - 1:
                    eol = '\n'
                else:
                    eol = ','
                print('(', coord[i][0], ',', coord[i][1],')', \
                      eol, sep= '', end='')

    return


##
##  Main routine
##
if __name__ == '__main__':
    
    tc = TestCase()
    
    solve(tc)
