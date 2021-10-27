"""
Program: dictionary_ops.py
Author: Andy Volesky
Last date modified: 10/27/2021
The purpose of this program:

Module: dictionary_ops that has 1 function
A function print_dict that accepts a dictionary and prints the pairs (key, value) one per line

"""

def print_dict(a_dict):
    for x in a_dict:
        print(x, a_dict[x])