from utility import *


def solve():
  rows=getOldAocInput(3)

  state=""
  num=""
  primoNum=0
  secondoNum=0
  ris=0
  doState=True
  for row in rows:
    for i in range(len(row)):
      element=row[i]

      if(element=="d" and state==""):
        state="d"
      elif(element=="o" and state=="d"):
        state="o"
      elif(element=="(" and state=="o"):
        state="("
      elif(element==")" and state=="("):
        state=""
        doState=True
      elif(element=="n" and state=="o"):
        state="n"
      elif(element=="'" and state=="n"):
        state="'"
      elif(element=="t" and state=="'"):
        state="t"
      elif(element=="(" and state=="t"):
        state="n("
      elif(element==")" and state=="n("):
        state=""
        doState=False
      elif(doState):
        if(element=="m" and state==""):
          state="m"
        elif(element=="u" and state=="m"):
          state="u"
        elif(element=="l" and state=="u"):
          state="l"
        elif(element=="(" and state=="l"):
          state="("
        elif(element.isdigit() and len(num)<3 and state in "(,"):
          num=num+element
        elif(element=="," and state=="(" and len(num)>0):
          primoNum=int(num)
          num=""
          state=","
        elif(element==")" and state=="," and len(num)>0):
          secondoNum=int(num)
          ris=ris+primoNum*secondoNum
          num=""
          state=""
        else:
          num=""
          state=""
      else:
          num=""
          state=""
  return ris

print(solve())
