import functools

from utilities import *


def parseArray(a):
  myArray=[]
  if(a[0]=='['):
    cursor=1
    for idx in range(1,len(a)):
      if(a[idx]=='['):
        cursor=cursor+1
      if(a[idx]==']'):
        cursor=cursor-1
        if(cursor==0):
          things=''
          secondCursor=0
          start=0
          for jdx in range(1,idx):
            if(a[jdx]=='['):
              if(secondCursor==0):
                start=jdx
              secondCursor=secondCursor+1
            elif(a[jdx]==']'):
              secondCursor=secondCursor-1
              if(secondCursor==0):
                myArray.append(parseArray(a[start:jdx+1]))
            elif(secondCursor==0):
              if(a[jdx]!=" " and a[jdx]!=","):
                things=things+a[jdx]
              else:
                if(len(things)>0):
                  myArray.append(int(things))    
                  things=''
          if(len(things)>0):
            myArray.append(int(things))
  else:
    return "error"
  return myArray            


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
      rightOrderResult=rightOrder([a[idx]], b[idx])
      if(rightOrderResult==0):
        continue
      else:
        return rightOrderResult
    if(isinstance(a[idx], list) and isinstance(b[idx], int)):
      rightOrderResult=rightOrder(a[idx], [b[idx]])
      if(rightOrderResult==0):
        continue
      else:
        return rightOrderResult

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
      a=parseArray(element)
    if(idx%3==1):
      b=parseArray(element)
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
    if(str(element)=='[[2]]' or str(element)=='[[6]]'):
      result=result*(idx+1)

  return result

print(solve())
print(solve2())