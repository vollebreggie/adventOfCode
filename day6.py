import string
import os
cwd = os.getcwd()

with open('input/6.txt') as f:
    initialPolymer = f.readline().strip()

print("Begin length: %s" % len(initialPolymer))
