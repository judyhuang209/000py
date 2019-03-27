# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 09:45:26 2019

@author: user
"""
import BubbleAndQuick

class pet():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __ge__(self, other):
        # greater than
        return self.age >= other.age
    
    def __str__(self):
        return self.name
    
    def __repr__(self):
        # allow to print objects as their names
        return self.name
    
    
pets = [pet('Justin', 1), pet('Bieber', 9), pet('Hailey', 9), pet('Selena', 4), pet('LeLe', 12)]


BubbleAndQuick.bubble_sort(5, pets)
#BubbleAndQuick.quick_sort(pets, 0, 4)
print(pets)