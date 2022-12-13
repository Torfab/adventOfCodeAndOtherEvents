from utilities import *
import functools

def rightOrder(a,b):
  paddingSize=abs(len(a)-len(b))
  resultIfFinish=0
  if(paddingSize>0):
    if(len(a)<len(b)):
      resultIfFinish=-1
    else:
      resultIfFinish=1

  for idx in range(max(len(a),len(b))-paddingSize):
    if(isinstance(a[idx], int) and isinstance(b[idx], list)):
      a[idx]=[a[idx]]
    if(isinstance(a[idx], list) and isinstance(b[idx], int)):
      b[idx]=[b[idx]]

    if(isinstance(a[idx], int) and isinstance(b[idx], int)):
      if(a[idx]==b[idx]):
        continue
      if(a[idx]<b[idx]):
        return -1
      if(a[idx]>b[idx]):
        return 1

    if(isinstance(a[idx], list) and isinstance(b[idx], list)):
      result=rightOrder(a[idx],b[idx])
      if (result!=0):
        return result

  return resultIfFinish

def solve():
  rows=getAocInput(13)
  result=0

  for idx, element in enumerate(rows):
    if(idx%3==0):
      a=eval(element)
    if(idx%3==1):
      b=eval(element)
      if(rightOrder(a,b)==-1):
        result=result+1+idx//3

  return result

def solve2():
  rows=getAocInput(13)
  
  arrayOfAll=[]

  for idx, element in enumerate(rows):
    if(idx%3==0):
      a=eval(element)
      arrayOfAll.append(a)
    if(idx%3==1):
      b=eval(element)
      arrayOfAll.append(b)

  arrayOfAll.append([[2]])
  arrayOfAll.append([[6]])

  newArray=sorted(arrayOfAll, key=functools.cmp_to_key(rightOrder))

  result=1
  for idx, element, in enumerate(newArray):
    if(len(element)==1):
      a=element.copy()
      while(isinstance(a,list) and len(a)==1):
        a=a[0]
      if(a==2 or a==6):
        result=result*(idx+1)

  return result

print(solve())
print(solve2())