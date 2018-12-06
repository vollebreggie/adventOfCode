import string
import os

cwd = os.getcwd()

class node:
    "A node in a grid"
    x = 0
    y = 0
    def infectNeightbors():
        #also diagonal or not?

with open('input/6.txt') as f:
    gridText = f.readlines()
    gridPoints = []

    for line in gridText:
       gridPoints.append(list(map(int, line.replace("\n", "").split(","))))
    
    biggestNumber = 356 #max problably only measures the first column
print("hello")
