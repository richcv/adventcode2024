#!/usr/bin/python3
import os
from pathlib import Path

#INPUT_FILE = "inputsample2.txt"
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
# ParseTheList1
# ---------------------------------------------------  
def ParseTheList1(bigList):

   totalCount = 0

   activeMode = True

   theMulTemplate = "mul(nnn,nnn)"
   theDontTemplate = "don't()"
   theDoTemplate = "do()"

   for rowIndex in range(len(bigList)):
      print (f"Checking line #{rowIndex}...")
      theMulTemplateIndex = 0
      theDoTemplateIndex = 0
      theDontTemplateIndex = 0

      for colIndex in range(len(bigList[rowIndex])):
         theVal = bigList[rowIndex][colIndex]

         if (theMulTemplateIndex == 4):
            #print ("SHOWTIME!")
            theMulTemplateIndex = 0
            if (activeMode):
               
               subby = bigList[rowIndex][colIndex:colIndex+8]

               parenIndex = subby.find(')')  # Find the index of the first ')'

               if parenIndex != -1:
                  substring = subby[:parenIndex]  #

                  #substring = my_string[start:start+6]
                  print(f"look at this: [{substring}]")

                  splitty = substring.split(',')
                  if (len(splitty) == 2):
                     if (splitty[0].isdigit() and splitty[1].isdigit()):
                        totalCount = totalCount + (int(splitty[0]) * int(splitty[1]))

         if (theMulTemplate[theMulTemplateIndex] == theVal):
            #print (f"matched {theVal}")
            theMulTemplateIndex += 1
         else:
            theMulTemplateIndex = 0
         #endif

         if (theDoTemplate[theDoTemplateIndex] == theVal):
            #print (f"matched {theVal}")
            theDoTemplateIndex += 1
            if (theDoTemplateIndex >= len(theDoTemplate)):
               print (f"{bcolors.BOLD_GREEN}DO!{bcolors.RESET}")
               theDoTemplateIndex = 0
               activeMode = True
         else:
            theDoTemplateIndex = 0
         #endif

         if (theDontTemplate[theDontTemplateIndex] == theVal):
            #print (f"matched {theVal}")
            theDontTemplateIndex += 1
            if (theDontTemplateIndex >= len(theDontTemplate)):
               print (f"{bcolors.BOLD_RED}DONT!{bcolors.RESET}")
               theDontTemplateIndex = 0
               activeMode = False
         else:
            theDontTemplateIndex = 0
         #endif

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
totalCount = ParseTheList1(theData)

print (f"Total Count: {bcolors.BOLD_GREEN}{totalCount}{bcolors.RESET}")

print(f"{bcolors.BOLD_RED}PEACE OUT HOMEY!{bcolors.RESET}")
   