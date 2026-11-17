from utility import *

def parseRows(rows):
  return list(rows[0])

def findNextCursors(letter, cursor, lastCursor, row):
  while(row[lastCursor]!=letter and lastCursor!=cursor):
    lastCursor=lastCursor-1
  while(row[cursor]==letter) and lastCursor!=cursor:
    cursor=cursor+1
  return cursor, lastCursor

def fixLetter(letter, row):
  cursor=row.index(letter)
  step=0
  movedElements=0
  lastIndex=len(row)-1

  cursor, lastCursor=findNextCursors(letter, cursor, lastIndex, row)
  if(cursor==lastCursor):
    return 0, lastIndex, row, movedElements

  while(cursor!=lastCursor):
    # print(cursor, lastCursor)
    step=step+1
    movedElements=movedElements+lastCursor-cursor+1
    row=row[:cursor]+list(reversed(row[cursor:lastCursor+1]))+row[lastCursor+1:]
    cursor, lastCursor=findNextCursors(letter, cursor, lastCursor, row)

  return step, cursor, row, movedElements

# def fixLetter2(letter, row):
#   cursor=row.index(letter)
#   step=0
#   lastIndex=len(row)-1

#   cursor, lastCursor=findNextCursors(letter, cursor, lastIndex, row)
#   if(cursor==lastCursor):
#     return 0, lastIndex, row

#   while(cursor!=lastCursor):
#     print(cursor, lastCursor)
#     step=step+lastCursor-cursor+1
#     row=row[:cursor]+list(reversed(row[cursor:lastCursor+1]))+row[lastCursor+1:]
#     cursor, lastCursor=findNextCursors(letter, cursor, lastCursor, row)

#   return step, cursor, row

  return step, cursor, row


def fixLetter3(innerRow, repetition):
  letter=innerRow[0]
  row=innerRow*2

  lenRow=len(innerRow)
  print("".join(row), lenRow, "LAVORO CON")
  step2, cursor, row, movedElements=fixLetter(letter, row)
  if(movedElements==0):
    return 0, innerRow, True

  #Somma di tutte le parti interne moltiplicat ala grandezza e gli step normali che fa, in aggiunta a quelli che si spostano esternamente moltiplicato per i turni 
  realStep=(((repetition-4)*repetition)//8)*lenRow//2*(step2+1)+movedElements*repetition//4
  
  realInnerRow=row[cursor+1:]
  print("A", "".join(realInnerRow))
  lenRealInnerRow=len(realInnerRow)
  realInnerRow=realInnerRow[:lenRealInnerRow//2]
  print("B", "".join(realInnerRow))

  return realStep, realInnerRow, False

  #CAPIRE QUANTO FA
  #CAPIRE COSA RIMANE



def solve():
  rows=openFile("raw.txt")
  row=parseRows(rows)

  letter=row[0]
  lenRow=len(row)

  step=0
  
  while(True):
    innerStep, cursor, row, _=fixLetter(letter, row)
    step=step+innerStep
    if(cursor==lenRow-1):
      return step
    letter=row[cursor+1]

def solve2(part, repetition):
  rows=openFile("raw.txt")
  innerRow=parseRows(rows)
  if(part==2):
    row=innerRow*repetition
  if(part==3):
    row=innerRow*100

  letter=row[0]
  lenRow=len(row)

  step=0
  
  while(True):
    _, cursor, row, innerStep=fixLetter(letter, row)
    print("fatto", innerStep)
    step=step+innerStep
    if(cursor==lenRow-1):
      return step
    letter=row[cursor+1]

def solve3(part, repetition):
  rows=openFile("raw.txt")
  innerRow=parseRows(rows)
  step=0
  innerRow=innerRow*2
  while(True):
    innerStep, innerRow, finish=fixLetter3(innerRow, repetition)
    print("QUACK", "".join(innerRow), innerStep)
    step=step+innerStep
    print(innerRow)
    if(finish):
      return step

print(solve2(2, 100))
print(solve3(2, 100))
