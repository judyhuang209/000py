# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 11:21:04 2019

@author: user
"""

def bubble_sort (n, s):
    count = 0
    for i in range (n - 1):
        swapped= False
        for j in range (n - 1 - i):
            if s[j] >= s[j + 1]:
                s[j], s[j + 1] = s[j + 1], s[j]
                swapped = True
                count += 1
        if swapped == False:
            break

def quick_sort(list, left, right): #in-place
    if left >= right:
        return list
    key = list[left]
    left_pivot = left
    right_pivot = right
    while left_pivot < right_pivot:
        while left_pivot < right_pivot and list[right_pivot] >= key: #從左向右找小於key值的
            right_pivot = right_pivot - 1
        while left_pivot < right_pivot and list[left_pivot] <= key: #從右向左找大於key值的
            left_pivot = left_pivot + 1
        if left_pivot < right_pivot:
            list[left_pivot], list[right_pivot] = list[right_pivot], list[left_pivot]
    list[left], list[left_pivot] = list[left_pivot], list[left] #跟key值交換
    quick_sort(list, left, left_pivot - 1)
    quick_sort(list, right_pivot + 1, right)
    return list