"""
Program: module_use.py
Author: Andy Volesky
Last date modified: 10/27/2021
The purpose of this program:

Write a file that uses your module my_definitions.py

"""

import my_definitions as md

if __name__ == "__main__":
    md.greet()
    md.author()
    md.print_dict(dict(key1=50, key2=100, key3=150, key4=9000))
    md.print_set({"sets", "are", "not", "ordered"})

