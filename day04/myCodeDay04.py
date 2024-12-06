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
# checkVal
# ---------------------------------------------------  
def checkVal(bigList, x, y, val):
   checksOut = False
   #print (f"[CHECK POS [{x},{y}] - limit to {len(bigList[0])},{len(bigList)}]", end= " ")
   if ((x >= 0) and (x < len(bigList[0])-1) and (y >= 0) and (y < len(bigList))):
      #print (f"[FOUND: '{bigList[x][y]}', EXPECTING: '{val}']",end = " ")
      if (bigList[x][y] == val):
         checksOut = True
   return checksOut
#end checkVal

# ---------------------------------------------------
# ParseTheList1
# ---------------------------------------------------  
def ParseTheList1(bigList):

   totalCount = 0

   for rowIndex in range(len(bigList)):
      #print (f"Checking line #{rowIndex}...")
      for colIndex in range(len(bigList[rowIndex])):

         theVal = bigList[rowIndex][colIndex]

         if (theVal == "X"):
            print(f"Hey its an X at {rowIndex},{colIndex}")
            #  DIRECTIONS
            #  0   1   2
            #  3   X   4
            #  5   6   7
            for direction in range(8):
               isGood = False
               print(f"Check direction {direction}", end=" ")
               if (direction == 0):
                  if (checkVal(bigList,rowIndex-1,colIndex-1,'M')) and \
                     (checkVal(bigList,rowIndex-2,colIndex-2,'A')) and \
                     (checkVal(bigList,rowIndex-3,colIndex-3,'S')):
                     isGood = True
               if (direction == 1):
                  if (checkVal(bigList,rowIndex-1,colIndex,'M')) and \
                     (checkVal(bigList,rowIndex-2,colIndex,'A')) and \
                     (checkVal(bigList,rowIndex-3,colIndex,'S')):
                     isGood = True
               if (direction == 2):
                  if (checkVal(bigList,rowIndex-1,colIndex+1,'M')) and \
                     (checkVal(bigList,rowIndex-2,colIndex+2,'A')) and \
                     (checkVal(bigList,rowIndex-3,colIndex+3,'S')):
                     isGood = True
               if (direction == 3):
                  if (checkVal(bigList,rowIndex,colIndex-1,'M')) and \
                     (checkVal(bigList,rowIndex,colIndex-2,'A')) and \
                     (checkVal(bigList,rowIndex,colIndex-3,'S')):
                     isGood = True
               if (direction == 4):
                  if (checkVal(bigList,rowIndex,colIndex+1,'M')) and \
                     (checkVal(bigList,rowIndex,colIndex+2,'A')) and \
                     (checkVal(bigList,rowIndex,colIndex+3,'S')):
                     isGood = True

               if (direction == 5):
                  if (checkVal(bigList,rowIndex+1,colIndex-1,'M')) and \
                     (checkVal(bigList,rowIndex+2,colIndex-2,'A')) and \
                     (checkVal(bigList,rowIndex+3,colIndex-3,'S')):
                     isGood = True
               if (direction == 6):
                  if (checkVal(bigList,rowIndex+1,colIndex,'M')) and \
                     (checkVal(bigList,rowIndex+2,colIndex,'A')) and \
                     (checkVal(bigList,rowIndex+3,colIndex,'S')):
                     isGood = True
               if (direction == 7):
                  if (checkVal(bigList,rowIndex+1,colIndex+1,'M')) and \
                     (checkVal(bigList,rowIndex+2,colIndex+2,'A')) and \
                     (checkVal(bigList,rowIndex+3,colIndex+3,'S')):
                     isGood = True


               if (isGood):
                  print (f"{bcolors.BOLD_GREEN}OK{bcolors.RESET}")
                  totalCount += 1
               else:
                  print (f"{bcolors.BOLD_RED}NOPE{bcolors.RESET}")

      #endif
   #endfor

   return totalCount
#end


# ---------------------------------------------------
# ParseTheList2
# ---------------------------------------------------  
def ParseTheList2(bigList):

   totalCount = 0

   for rowIndex in range(len(bigList)):
      #print (f"Checking line #{rowIndex}...")
      for colIndex in range(len(bigList[rowIndex])):

         theVal = bigList[rowIndex][colIndex]

         if (theVal == "A"):
            isGood = False
            print(f"Hey its an A at {rowIndex},{colIndex}", end = " ")
            #  DIRECTIONS
            #  0   1   2
            #  3   X   4
            #  5   6   7

            downslope =  ((checkVal(bigList,rowIndex-1,colIndex-1,'M')) and \
                          (checkVal(bigList,rowIndex+1,colIndex+1,'S'))) or \
                          ((checkVal(bigList,rowIndex-1,colIndex-1,'S')) and \
                           (checkVal(bigList,rowIndex+1,colIndex+1,'M')))

            upslope =  ((checkVal(bigList,rowIndex+1,colIndex-1,'M')) and \
                        (checkVal(bigList,rowIndex-1,colIndex+1,'S'))) or \
                       ((checkVal(bigList,rowIndex+1,colIndex-1,'S')) and \
                        (checkVal(bigList,rowIndex-1,colIndex+1,'M')))

            if (upslope and downslope):
               isGood = True

            if (isGood):
               print (f"{bcolors.BOLD_GREEN}OK{bcolors.RESET}")
               totalCount += 1
            else:
               print (f"{bcolors.BOLD_RED}NOPE{bcolors.RESET}")

      #endif
   #endfor

   return totalCount
#end

# ---------------------------------------------------
# ReadTheInput
# ---------------------------------------------------   
def ReadTheInput():

   script_path = os.path.realpath(__file__)

   script_dir = os.path.dirname(script_path)
   FILE = os.path.join(script_dir, INPUT_FILE)

   theBigList = []
   with open(FILE) as f:
      for line in f:
         theBigList.append(line)
      #endfor
   #endwith
      
   return theBigList
#end ReadTheInput

# ---------------------------------------------------
# Main
# ---------------------------------------------------   

theData = ReadTheInput()
#successCount = ParseTheList(theData)
#totalCount = ParseTheList1(theData)
totalCount = ParseTheList2(theData)

print (f"Total Count: {bcolors.BOLD_GREEN}{totalCount}{bcolors.RESET}")

print(f"{bcolors.BOLD_RED}PEACE OUT HOMEY!{bcolors.RESET}")
   