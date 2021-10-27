"""
Program: package_use.py
Author: Andy Volesky
Last date modified: 10/27/2021
The purpose of this program:

Write a file that uses your package definitions

"""

import definitions.greeting as gt
import definitions.dicitonary_ops as do
import definitions.set_ops as so

if __name__ == "__main__":
    gt.greet()
    gt.author()
    do.print_dict(dict(key1=50, key2=100, key3=150, key4=9000))
    so.print_set({"sets", "are", "not", "ordered"})
