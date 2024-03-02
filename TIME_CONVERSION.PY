#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    string = s.split(':')
    start_index = int(string[0])
    last_index = string[-1]
    last_index1 = ''.join(char for char in last_index if not char.isdigit())
    if start_index==12 and last_index1 == 'AM':
        string[0] = str(00)
        string[-1] = ''.join(char for char in last_index if  char.isdigit())
        s = ':'.join(string)
    elif last_index1 == 'AM':
        string[-1] = ''.join(char for char in last_index if  char.isdigit())
        s = ':'.join(string)
    elif last_index1 == 'PM':
        string[0]=str(start_index + 12)
        string[-1] = ''.join(char for char in last_index if  char.isdigit())
        s = ':'.join(string)
        
    
        
    #start_index = str(start_index + 12)
    
    #string[0] = start_index
    #string[-1] = last_index
    #s = ':'.join(string)
    print(type(s))
    
    return s
    
s = input("Enter time: ")

result = timeConversion(s)
print(result)

   