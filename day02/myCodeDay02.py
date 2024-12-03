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
# ParseTheList
# ---------------------------------------------------  
def ParseTheList(bigList):
   successCount = 0
   for rowIndex in range(len(bigList)):
      firstNum = True
      prevVal = 0
      prevDiff = 0
      isGood = True
      print (f"Checking {bigList[rowIndex]}...", end=" ")
      for colIndex in range(len(bigList[rowIndex])):
         theVal = int(bigList[rowIndex][colIndex])
         if (firstNum):
            firstNum = False
         else:
            diff = theVal - prevVal

            if (abs(diff) > 3) or (diff == 0):
               print(f"{bcolors.RED}BAD cuz col:{colIndex} is too far away{bcolors.RESET}")
               isGood = False
               break
            else:
               if ((diff < 0) and (prevDiff > 0)) or ((diff > 0) and (prevDiff < 0)):
                  print(f"{bcolors.RED}BAD cuz col:{colIndex} went the other direction.{bcolors.RESET}")
                  isGood = False
                  break
               #endif
            #endif
            prevDiff = diff
         #endif
         
         prevVal = theVal
      #endfor
      if (isGood):
         print(f"{bcolors.BOLD_GREEN}GOOD!{bcolors.RESET}")
         successCount += 1
   #endfor

   return successCount
#end

# ---------------------------------------------------
# CheckTheRow
# ---------------------------------------------------  
def CheckTheRow(theRow):
   firstNum = True
   prevVal = 0
   prevDiff = 0
   isGood = True
   print (f"Checking {theRow}...", end=" ")
   for colIndex in range(len(theRow)):
      theVal = int(theRow[colIndex])
      if (firstNum):
         firstNum = False
      else:
         diff = theVal - prevVal

         if (abs(diff) > 3) or (diff == 0):
            print(f"{bcolors.RED}BAD cuz col:{colIndex} is too far away{bcolors.RESET}")
            isGood = False
            break
         else:
            if ((diff < 0) and (prevDiff > 0)) or ((diff > 0) and (prevDiff < 0)):
               print(f"{bcolors.RED}BAD cuz col:{colIndex} went the other direction.{bcolors.RESET}")
               isGood = False
               break
            #endif
         #endif
         prevDiff = diff
      #endif
      
      prevVal = theVal
   #endfor

   return isGood
#end

# ---------------------------------------------------
# ParseTheList3
# ---------------------------------------------------  
def ParseTheList3(bigList):
   successCount = 0
   for rowIndex in range(len(bigList)):
      success = CheckTheRow(bigList[rowIndex])
      if (success):
         print(f"{bcolors.BOLD_GREEN}GOOD!{bcolors.RESET}")
         successCount += 1
      else:
         print(f"{bcolors.BOLD_MAGENTA}BACKUP PLAN.  LETS TRY SKIPPING{bcolors.RESET}")
         for colIndex in range(len(bigList[rowIndex])):
            tempList = bigList[rowIndex]
            new_list = tempList[:colIndex] + tempList[colIndex+1:]
            print(f"Lets try without {colIndex}")
            #tempList.pop(int(colIndex))
            success = CheckTheRow(new_list)
            if (success):
               print(f"{bcolors.BOLD_GREEN}GOOD!{bcolors.RESET}")
               successCount += 1
               break
   #endfor

   return successCount
#end ParseTheList3

# ---------------------------------------------------
# ParseTheList2
# ---------------------------------------------------  
def ParseTheList2(bigList):
   successCount = 0
   for rowIndex in range(len(bigList)):
      firstNum = True
      prevVal = 0
      prevDiff = 0
      isGood = True
      skipHit = False
      skipThis = False
      print (f"Checking {bigList[rowIndex]}...", end=" ")
      for colIndex in range(len(bigList[rowIndex])):
         theVal = int(bigList[rowIndex][colIndex])
         if (firstNum):
            firstNum = False
         else:
            diff = theVal - prevVal

            if (abs(diff) > 3) or (diff == 0):
               if (not skipHit):
                  print (f"{bcolors.BLUE}SKIP Col:{colIndex}{bcolors.RESET}", end=" ")
                  skipThis = True
               else:
                  print(f"{bcolors.RED}BAD cuz col:{colIndex} is too far away{bcolors.RESET}")
                  isGood = False
                  break
            else:
               if ((diff < 0) and (prevDiff > 0)) or ((diff > 0) and (prevDiff < 0)):
                  if (not skipHit):
                     print (f"{bcolors.BLUE}SKIP Col:{colIndex}{bcolors.RESET}", end=" ")
                     skipThis = True
                  else:
                     print(f"{bcolors.RED}BAD cuz col:{colIndex} went the other direction.{bcolors.RESET}")
                     isGood = False
                     break
               #endif
            #endif
            if (not skipThis):
               prevDiff = diff
         #endif
         
         if (not skipThis):
            prevVal = theVal
         else:
            skipHit = True
      #endfor
      if (isGood):
         print(f"{bcolors.BOLD_GREEN}GOOD!{bcolors.RESET}")
         successCount += 1
   #endfor

   return successCount
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
         newLine = []
         theSplitLine = line.split(' ')
         #print (f"LINE: <{theLine}>")
         firstPart = True
         for derp in theSplitLine:
            if len(derp.strip()) > 0:
               newLine.append(derp.strip())
            #endif
         #endfor
         theBigList.append(newLine)
      #endfor
   #endwith
      
   return theBigList

# ---------------------------------------------------
# Main
# ---------------------------------------------------   

theData = ReadTheInput()
#successCount = ParseTheList(theData)
successCount = ParseTheList3(theData)

print (f"Success Count: {bcolors.BOLD_GREEN}{successCount}{bcolors.RESET} (out of {len(theData)})")

print(f"{bcolors.BOLD_RED}PEACE OUT HOMEY!{bcolors.RESET}")
   