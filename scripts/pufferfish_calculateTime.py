#!/usr/bin/env python3
import re 
import sys

def calTime(fname): 
    f = open(fname, "r")
    contents = f.read()
    f.close()
    matched_lines = re.findall("^Time for querying: [0-9]+ ns", contents, re.M)
    time = 0
    for item in matched_lines: 
        x = re.sub("Time for querying: ", "", item)
        x = re.sub(" ns", "", x)
        time += int(x)
    print(fname + " query time: " + str(time))
    return time

def main(argv):
    calTime(argv)


if __name__ == "__main__":
    main(sys.argv[1])
