from utility import *

def parseRows(row, length):

  newRows=[]
  substring=""
  for i in range(len(row)):
    substring=substring+row[i]
    if((i+1)%length==0):
      newRows.append(substring)
      substring=""
  return newRows

def addFightValue(c):
  if(c=="B"):
    return 1
  if(c=="C"):
    return 3
  if(c=="D"):
    return 5
  return 0
  

def solve(divide):
  rows=openFile("raw.txt")
  rows=parseRows(rows[0],divide)
  
  counter=0

  for element in rows:
    missings=element.count("x")
    subcounter=0
    if (divide-missings==3):
      subcounter=subcounter+6
    if (divide-missings==2):
      subcounter=subcounter+2

    for i in range(divide):
      subcounter=subcounter+addFightValue(element[i])
    if(subcounter<0):
      subcounter=0

    counter=counter+subcounter
    
  return counter

print(solve(1))
print(solve(2))
print(solve(3))
