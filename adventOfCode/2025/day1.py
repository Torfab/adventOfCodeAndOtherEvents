from utility import *

def parseRows(rows):
  orders=[]
  for row in rows:
    direction=row[0]
    quantity=int(row[1:])
    orders.append((direction, quantity))
  return orders

def solve():
  rows=getOldAocInput(1)
  orders=parseRows(rows)
  size=100
  current=50
  count=0
  for order in orders:
    if order[0]=="R":
      direction= 1
    if order[0]=="L":
      direction= -1
    current=(current+direction*order[1])%size
    if current==0:
      count=count+1
  return count
    
def solve2():
  rows=getOldAocInput(1)
  orders=parseRows(rows)
  size=100
  current=50
  count=0
  for order in orders:
    if order[0]=="R":
      direction= 1
    if order[0]=="L":
      direction= -1
    count=count+order[1]//100
    realOrder=order[1]%size
    newPosition=(current+direction*realOrder)
    if current!=0 and (newPosition<=0 or newPosition>=100):
      count=count+1
    current=newPosition%size
  return count

print(solve())
print(solve2())
