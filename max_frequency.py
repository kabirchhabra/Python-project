# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def most_frequent(input):
    res = {}
    for i in input:
        res[i] = res.get(i,0) + 1
    print(str(res))
        

s = input("Input : ")
most_frequent(s)

