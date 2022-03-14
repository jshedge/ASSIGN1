#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 15:50:31 2022

@author: Jamie
"""

from tenacity import retry


question_list = ['What is your favourite food?', 'What is your favourite film?']

def question_response(question):
    print (f"Please type the answer to the following question: {question}")
    answer = input()
    print ("Your word contains", len(answer), ("letters"))
    return answer
    
def number_response(answer):
    print ("type a number")
    response = input()
    number = int(response)
    finalanswer = (number + (len(answer)))
    first_answer = f"The total number of letters in your word added to your number is {finalanswer}"
    print (first_answer)
    return number

def second_number_response(number, answer):
    print ("type another number")
    response2 = input()
    number2 = int(response2)
    finalanswer = (number + (len(answer)))
    finalanswer2 = (number2 + (len(answer)))
    second_answer =  f"The total number of letters in your word added to your number and your second number is {finalanswer} and {finalanswer2}"
    return print(second_answer)


for question in question_list:
    answer = question_response(question)
    number = number_response(answer)
    second_number_response(number, answer)