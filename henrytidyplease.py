#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 15:50:31 2022

@author: Jamie
"""

question = ("Type in any word")
print (question)
answer = input()
print ("Your word contains", len(answer), ("letters"))

print ("type a number")
response = input()
number = int(response)
print ("The total number of letters in your word added to your number is...", number + (len(answer)))

#################################################################
#You can use  %s in place of "," or "+". See below

question = ("Type in any word")
print (question)
answer = input()
print ("Your word contains", len(answer), ("letters"))

print ("type a number")
response = input()
number = int(response)
finalanswer = (number + (len(answer)))
print ("The total number of letters in your word added to your number is... %s" % finalanswer)

#################################################################

question = ("Type in any word")
print (question)
answer = input()
print ("Your word contains", len(answer), ("letters"))

print ("type a number")
response = input()
number = int(response)
print ("type another number")
response2 = input()
number2 = int(response2)
finalanswer = (number + (len(answer)))
finalanswer2 = (number2 + (len(answer)))
print ("The total number of letters in your word added to your number and your second number is... %s and %s" % (finalanswer, finalanswer2))
                                                                                         
                                                                                
                                                                                    
