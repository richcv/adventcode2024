#!/usr/bin/python3
import os
from pathlib import Path

#INPUT_FILE = "inputsample.txt"
INPUT_FILE = "input01.txt"
list1 = []
list2 = []

class bcolors:
    # Standard Colors
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    
    # Bold Colors
    BOLD_BLACK = "\033[1;30m"
    BOLD_RED = "\033[1;31m"
    BOLD_GREEN = "\033[1;32m"
    BOLD_YELLOW = "\033[1;33m"
    BOLD_BLUE = "\033[1;34m"
    BOLD_MAGENTA = "\033[1;35m"
    BOLD_CYAN = "\033[1;36m"
    BOLD_WHITE = "\033[1;37m"
    
    # Reset
    RESET = "\033[0m"

# ---------------------------------------------------
# DoPart1
# ---------------------------------------------------  
def DoPart1(list1, list2):
   totalVal = 0
   for numIndex in range(len(list1)):
      #print(f"{list1[numIndex]} and {list2[numIndex]}")
      totalVal = totalVal + abs(int(list1[numIndex]) - int(list2[numIndex]))
   print (f"Part1 Final: {bcolors.BOLD_GREEN}{totalVal}{bcolors.RESET}")

# ---------------------------------------------------
# DoPart2
# ---------------------------------------------------  
def DoPart2(list1, list2):
   totalVal = 0
   for numIndex in range(len(list1)):
      firstNum = list1[numIndex]
      theCount = list2.count(firstNum)
      totalVal = totalVal + (int(firstNum) * theCount)
      #print(f"{list1[numIndex]} and {list2[numIndex]}")
      #totalVal = totalVal + abs(int(list1[numIndex]) - int(list2[numIndex]))
   print (f"Part2 Final: {bcolors.BOLD_GREEN}{totalVal}{bcolors.RESET}")

# ---------------------------------------------------
# Main
# ---------------------------------------------------   
script_path = os.path.realpath(__file__)

script_dir = os.path.dirname(script_path)
FILE = os.path.join(script_dir, INPUT_FILE)

with open(FILE) as f:
   for line in f:
      theLine = line.split(' ')
      #print (f"LINE: <{theLine}>")
      firstPart = True
      for derp in theLine:
         if len(derp.strip()) > 0:
            if firstPart:
               firstPart = False
               list1.append(derp.strip())
            else:
               list2.append(derp.strip())
            #endif
         #endif
      #endfor
   #endfor
#endwith
   
list1.sort()
list2.sort()

DoPart1(list1, list2)
DoPart2(list1, list2)
print(f"{bcolors.BOLD_RED}PEACE OUT HOMEY!{bcolors.RESET}")
   