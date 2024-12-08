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
def ParseTheList1(ruleList, updateList):

   totalCount = 0

   for updateGuy in updateList:
      isUpdateGood = True

      print (f"Check this here update {updateGuy}...", end = " ")
      middlePageVal = int(updateGuy[int(len(updateGuy) / 2)])

      for ruleGuy in ruleList:
         if (ruleGuy[0] in updateGuy) and (ruleGuy[1] in updateGuy):
            leftIndex = updateGuy.index(ruleGuy[0])
            rightIndex = updateGuy.index(ruleGuy[1])
            if rightIndex < leftIndex:
               isUpdateGood = False
               print (f"{bcolors.BOLD_RED}FAILED THIS RULE {ruleGuy}{bcolors.RESET}", end =" ")
               break



      if (isUpdateGood):
         print (f"{bcolors.BOLD_GREEN}OK! Add: {middlePageVal}{bcolors.RESET}")
         totalCount += middlePageVal
      else:
         print (f"{bcolors.BOLD_RED}NOPE!{bcolors.RESET}")
      #endif
   #endfor

   return totalCount
#end


# ---------------------------------------------------
# ParseTheList2
# ---------------------------------------------------  
def ParseTheList2(ruleList, updateList):

   totalCount = 0

   for updateGuy in updateList:
      isUpdateGood = False

      print (f"Check this here update {updateGuy}...", end = " ")

      swappyState = True
      while swappyState:
         swappyState = False
         for ruleGuy in ruleList:
            if (ruleGuy[0] in updateGuy) and (ruleGuy[1] in updateGuy):
               leftIndex = updateGuy.index(ruleGuy[0])
               rightIndex = updateGuy.index(ruleGuy[1])
               if rightIndex < leftIndex:
                  isUpdateGood=True
                  swappyState= True
                  print(f"{bcolors.BOLD_CYAN}swappin {ruleGuy[1]} and {ruleGuy[0]} '{bcolors.RESET}", end = " ")
                  updateGuy[leftIndex] = ruleGuy[1]
                  updateGuy[rightIndex] = ruleGuy[0]



      if (isUpdateGood):
         middlePageVal = int(updateGuy[int(len(updateGuy) / 2)])
         print(f"Final:{updateGuy}", end = " ")
         print (f"{bcolors.BOLD_GREEN}OK! Add: {middlePageVal}{bcolors.RESET}")
         totalCount += middlePageVal
      else:
         print (f"{bcolors.BOLD_RED}NOPE!{bcolors.RESET}")
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

   inDaRules = True
   theRules = []
   theUpdates = []
   with open(FILE) as f:
      for line in f:
         if (len(line.strip()) == 0) and (inDaRules):
            inDaRules = False
         else:
            if (inDaRules):
               theRules.append(line.strip().split('|'))
            else:
               theUpdates.append(line.strip().split(','))
      #endfor
   #endwith
      
   return theRules, theUpdates
#end ReadTheInput

# ---------------------------------------------------
# Main
# ---------------------------------------------------   

theRules,thePages = ReadTheInput()
#successCount = ParseTheList(theData)
#totalCount = ParseTheList1(theData)
#totalCount = ParseTheList1(theRules, thePages)
totalCount = ParseTheList2(theRules, thePages)

print (f"Total Count: {bcolors.BOLD_GREEN}{totalCount}{bcolors.RESET}")

print(f"{bcolors.BOLD_RED}PEACE OUT HOMEY!{bcolors.RESET}")
   