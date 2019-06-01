#! /usr/bin/env python3.1
import fileinput

def main():
    
    for line in fileinput.input():
        if not line.startswith('##'):
            print(line, end="")
#main()
