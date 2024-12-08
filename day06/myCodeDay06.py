#!/usr/bin/python3
import os
from pathlib import Path

#INPUT_FILE = "inputsample.txt"
INPUT_FILE = "input01.txt"

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
# ReadTheInput
# ---------------------------------------------------   
def ReadTheInput():

   script_path = os.path.realpath(__file__)

   script_dir = os.path.dirname(script_path)
   FILE = os.path.join(script_dir, INPUT_FILE)

   theData = []
   with open(FILE) as f:
      for line in f:
         theData.append(line.strip())
      
   return theData
#end ReadTheInput

# ---------------------------------------------------
# CheckSquare
# ---------------------------------------------------   
def CheckSquare(theData, xVal, yVal):
   returnVal = ""
   if (xVal < 0) or (yVal < 0) or (xVal >= len(theData[0])) or (yVal >= len(theData)):
      returnVal = "OOB"
   else:
      returnVal = theData[yVal][xVal]
   #endif
   return returnVal

# ---------------------------------------------------
# FindDude
# ---------------------------------------------------   
def FindDude(theData):
   xDude = -1
   yDude = -1

   for ySearch in range(len(theData)):
      for xSearch in range(len(theData[ySearch])):
         if (theData[ySearch][xSearch] == "^"):
            xDude = xSearch
            yDude = ySearch
            break

   return xDude, yDude 

# ---------------------------------------------------
# ParseTheList1
# ---------------------------------------------------   
def ParseTheList1(theData):


   #for x in theData:
   #    print(x)
   uniqueSpots = []
 
   # DIRECTIONS
   #     0
   #   3 + 1
   #     2
   direction = 0
   keepGoing = True
   xDude, yDude = FindDude(theData)
   print (f"Dude is at {xDude},{yDude}")
   uniqueSpots.append(f"{xDude},{yDude}")

   movements = 0

   #While not done
   while keepGoing:

      movements += 1
      if (movements > 9999):
         keepGoing = False

      xNext = xDude
      yNext = yDude
      print (f"Move #{movements}.  Dude at {xDude},{yDude}", end = " ")
      if (direction == 0):
         print (f"{bcolors.MAGENTA},Going N{bcolors.RESET}", end = " ")
         yNext = yNext - 1
      elif (direction == 1):
         print (f"{bcolors.MAGENTA},Going E{bcolors.RESET}", end = " ")
         xNext = xNext + 1
      elif (direction == 2):
         print (f"{bcolors.MAGENTA},Going S{bcolors.RESET}", end = " ")
         yNext = yNext + 1
      else:
         print (f"{bcolors.MAGENTA},Going W{bcolors.RESET}", end = " ")
         xNext = xNext - 1
      #endif
         
      #  Check square in next direction
      val = CheckSquare(theData, xNext, yNext)
      print (f"{bcolors.BLACK},Val={val}{bcolors.RESET}", end = " ")
      #  If its out of bounds, we done
      if (val == "OOB"):
         print(f"{bcolors.RED}DONE!{bcolors.RESET}")
         keepGoing = False
      #  Elseif its a blockade, change direction (direction + 1; if dir >3, dir = 0)
      elif (val == "#"):
         print(f"{bcolors.YELLOW}TURN RIGHT{bcolors.RESET}")
         direction += 1
         if direction > 3:
            direction = 0
         #endif
      #  Elseif its open, move the dude and add that square to the unique spots
      elif (val == ".") or (val == "^"):
         print(f"{bcolors.CYAN}Move it!{bcolors.RESET}", end = " ")
         xDude = xNext
         yDude = yNext
         posString = f"{xDude},{yDude}"
         if (posString in uniqueSpots):
            print (f"Don't add {posString}")
         else:
            print (f"(Added point {posString})")
            uniqueSpots.append(posString)
         #endif
      #endif
   #end while

   return len(uniqueSpots)

# ---------------------------------------------------
# Main
# ---------------------------------------------------   
theData = ReadTheInput()
totalCount = ParseTheList1(theData)
#totalCount = ParseTheList1(theRules, thePages)
#totalCount = ParseTheList2(theRules, thePages)

print (f"Total Count: {bcolors.BOLD_GREEN}{totalCount}{bcolors.RESET}")

print(f"{bcolors.BOLD_RED}PEACE OUT HOMEY!{bcolors.RESET}")
   