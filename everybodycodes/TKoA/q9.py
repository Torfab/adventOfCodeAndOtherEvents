from utility import *

possibleValues=[1,3,5,10]
possibleValues2=[1,3,5,10,15,16,20,24,25,30]
possibleValues3=[1, 3, 5, 10, 15, 16, 20, 24, 25, 30, 37, 38, 49, 50, 74, 75, 100, 101]

dizionarioDelResto={0:0}

def solve(coinValues):
  rows=openFile("raw.txt")
  rows=[int(x) for x in rows]
  myNum=max(rows)
  for coin in coinValues:
    for i in range(coin, myNum+1):
      if(dizionarioDelResto.get(i)==None):
        dizionarioDelResto[i]=dizionarioDelResto.get(i-coin)+1
      else:
        dizionarioDelResto[i]=min(dizionarioDelResto.get(i), dizionarioDelResto.get(i-coin)+1)
  count=0
  for myNum in rows:
    count=count+dizionarioDelResto[myNum]
  return count

def solve2(coinValues):
  rows=openFile("raw.txt")
  rows=[int(x) for x in rows]
  maxMyRows=max(rows)
  myNum=maxMyRows//2+100
  for coin in coinValues:
    for i in range(coin, myNum+1):
      if(dizionarioDelResto.get(i)==None):
        dizionarioDelResto[i]=dizionarioDelResto.get(i-coin)+1
      else:
        dizionarioDelResto[i]=min(dizionarioDelResto.get(i), dizionarioDelResto.get(i-coin)+1)


  count=0
  for myNum in rows:
    actualMin=maxMyRows//2+100
    for strife in range(0,51):
      if(myNum%2==0):
        num1=myNum//2-strife
        num2=myNum//2+strife
      else:
        if strife==50:
          continue
        considero=myNum+1
        num1=considero//2-strife-1
        num2=considero//2+strife
      currentMin=dizionarioDelResto[num1]+dizionarioDelResto[num2]
      if(currentMin<actualMin):
        actualMin=currentMin
    
    
    count=count+actualMin
  return count


print(solve(possibleValues))
print(solve(possibleValues2))
print(solve2(possibleValues3))


