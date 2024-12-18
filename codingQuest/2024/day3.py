from utility import *

def parseRows(rows):
  row=rows[0].strip()

  return [int(x) for x in row.split(" ")]

def solve():
  rows=openFile("input.txt")
  myArray=parseRows(rows)
  current="."
  resultArray=[]
  for element in myArray:
    for _ in range(element):
      resultArray.append(current)
    if(current=="."):
      current="#"
    else:
      current="."
    
  for i in range(len(resultArray)):
    print(resultArray[i], end="")
    if(i%100==0):
      print()
    

  return
print(solve())