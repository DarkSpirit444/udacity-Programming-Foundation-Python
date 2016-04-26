from __future__ import print_function
import sys

print("Four Calling Birds", "Three French Hens", "Two Turtle Doves", "and a Partridge in a Pear Tree.", sep=",", end="EOL", file=sys.stderr)

outputfile = open("test.txt", 'w+')

print("Four Calling Birds", "Three French Hens", "Two Turtle Doves", "and a Partridge in a Pear Tree.", sep=",", end="EOL", file=outputfile)

outputfile.close()
