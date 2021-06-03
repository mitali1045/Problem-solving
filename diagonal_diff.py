# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 15:45:31 2021

@author: Mitali.Tavildar
"""

def diagonalDifference(arr):
    left_d = []
    right_d = []
    for i in range(0,len(arr)):
        left_d.append(int(arr[i][i]))
        right_d.append(int(arr[i][n-1-i]))
    left_d = sum(left_d)
    right_d = sum(right_d)

    return(abs(left_d - right_d))