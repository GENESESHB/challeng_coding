#!/usr/bin/python3

""" this is a '0-reverse_string' moduls """


def reverse_string(string):


     reversed_string = ""

     for i in range(len(string) - 1, -1, -1):

          reversed_string += string[i]


     return reversed_string
