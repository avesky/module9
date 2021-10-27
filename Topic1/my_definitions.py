"""
Program: my_definitions.py
Author: Andy Volesky
Last date modified: 10/27/2021
The purpose of this program:

Write a Python module, called my_definitions that includes the following
A function greeting that prints a friendly greeting
A function message that prints you as the author of the code
A function print_dict that accepts a dictionary and prints the pairs (key, value) one per line
A function print_set that accepts a set and prints the set one item per line

"""

def greet():
    print("G'day Mate!")
def author():
    print("Program authored by Andrew Volesky")
def print_dict(a_dict):
    for x in a_dict:
        print(x, a_dict[x])
def print_set(a_set):
    for i in a_set:
        print(i)

