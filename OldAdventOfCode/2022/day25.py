from utilities import *

dictSnafuConversion={'=':-2, "-":-1, '0':0, '1':1, '2':2}
dictDecimalConversion={2:'2', 1:'1', 0:'0', -1:'-', -2:'='}

def sumTwoSnafuCharacters(a,b):
  result=dictSnafuConversion[a]+dictSnafuConversion[b]
  reminder=0
  if(result==4):
    reminder=1
    result='-'
  if(result==3):
    reminder=1
    result='='
  elif(result==-1):
    result='-'
  elif(result==-2):
    result='='
  elif(result==-3):
    result=2
    reminder='-'
  elif(result==-4):
    result=1
    reminder='-'
  # print("risultato", str(reminder), str(result))
  return (str(reminder), str(result))

def sumTwoSnafuNumber(a,b):
  distance=abs(len(a)-len(b))
  newLine=''
  for _ in range(distance):
    newLine=newLine+'0'
  if(len(a)< len(b)):
    a=newLine+a
  if(len(a)> len(b)):
    b=newLine+b

  # print("i numeri da sommare sono", a, b)

  reminder='0'
  result=''
  for idx in reversed(range(len(a))):
    reminderA, sum=sumTwoSnafuCharacters(a[idx], reminder)
    reminderB, sum=sumTwoSnafuCharacters(b[idx], sum)
    _, reminder=sumTwoSnafuCharacters(reminderA, reminderB)
    result=sum+result
  if (reminder!='0'):
    result=reminder+result

  return result

# print(sumTwoSnafuNumber('22',''))

# print(sumTwoSnafuNumber('1--20', '1-00==1-1=='))

def solve():
  rows=getAocInput(25)
  result=''
  for element in rows:
    result=sumTwoSnafuNumber(result, element)
  return result

print(solve())