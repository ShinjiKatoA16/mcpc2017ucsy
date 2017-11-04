#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
    2017 MCPC at UCSY
    Problem-I: Money Drop Game

    The description of this problem is not clear, and may be there are
    mistakes in the description or sample input/output.

    Assumes that the number of bundles to 20 (50 in description)
'''

NUM_BUNDLE = 20
KYAT_PER_BUNDLE = 500000

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
    tc.quiz = list()
    for i in range(tc.n):
        tc.quiz.append(sys.stdin.readline().split())

    return


def check_answer(quiz, num, correct_answer):
    '''
        quiz: List
        num:  String '0', '1', '2' or '3'
        correct_answer: String 'A', 'B', 'C' or 'D'

        return: None if num not found, True if match, Falase otherwise
    '''

#    print('check:', num, quiz, end = ' ')
    for i in range(len(quiz)-1):
        ans = quiz[i]
        if ans[1] == num:
            if ans[0] == correct_answer:
#                print(ans, 'is correct:', correct_answer)
                return True
            else:
#                print(ans, 'is not correct:', correct_answer)
                return False

    return None


def solve(tc):
    '''
        Input: Test Case
        Return: None
    '''

    parse_tc(tc)
    bundles = NUM_BUNDLE

    for quiz in tc.quiz:
        correct_answer = quiz[len(quiz)-1]
        for num in ('0', '1', '2', '3'):
            if num == '0' or num == '3': bank_up = bundles
            else: bank_up = bundles - (bundles // 3)

            is_match = check_answer(quiz, num, correct_answer)
            if is_match == None: continue
            elif is_match: break
            else:
                if num == '0' or num == '3':
                    print('sorry')
                    return
                else:
                    bundles -= bank_up
                    if bundles == 0:
                        print('sorry')
                        return
        else:
            print('Correct answer not found and money remains')
            raise ValueError

    print(bank_up * KYAT_PER_BUNDLE)
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
