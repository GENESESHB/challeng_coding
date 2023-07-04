#!/usr/bin/python3

""" this is a '1-count_vowels' moduls """


def count_vowels(string):
   
    string = string.lower()

    
    count = 0

    
    for char in string:
        if char in "aeiou":
            count += 1

    
    return count
