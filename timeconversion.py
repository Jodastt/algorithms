#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    if int s[:-2] = "PM":
        militaryTime = s[:-2]
        militaryTimeStart = int(militaryTime[2:])*2
        militaryTime = militaryTime[2:6]
        militaryTime = str(militaryTimeStart) + militaryTime
    elif int s[:-2] = "AM"
        militaryTime = s[:-2]
    return militaryTime

    if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
