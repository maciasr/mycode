#!/usr/bin/env python3
## create file object in "r"ead mode

filename = (input("What should the file name be? "))


with open("vlanconfig.cfg", "r") as filename:
    ## readlines() creates a list by reading target
    ## file line by line
    configlist = filename.readlines()

## file was just auto closed (no more indenting)

## each item of the list now has the "\n" characters back
    for x in configlist:
            print(x.strip()) 
