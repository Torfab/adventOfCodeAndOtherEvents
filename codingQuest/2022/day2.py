from utility import *

winningValues={0:0,1:0,2:0,3:1,4:10,5:100,6:1000}

def evaluate(rowList, winningElements):
  count=0
  for element in winningElements:
    if(element in rowList):
      count=count+1
  if(count>2):
    print(rowList, winningElements, "ho vinto", winningValues[count])
  return winningValues[count]

rows=openFile("input.txt")

winningElements="95,73,30,12,97,27".split(",")

accumulatore=0
for row in rows:
  accumulatore=accumulatore+evaluate(row.split(" "), winningElements)
print(accumulatore)