from utility import *

def buildDeclarationsForm(rows):
  declarationForms=[]
  
  singleGroup=[]
  for row in rows:
    if(row==""):
      declarationForms.append(singleGroup)
      singleGroup=[]
      continue
    singleGroup.append(row)
  declarationForms.append(singleGroup)
  return declarationForms

def checkValidA(form):
  questionAnswered=set()
  for singleForm in form:
    for singleQuestion in singleForm:
      questionAnswered.add(singleQuestion)
  return len(questionAnswered)

def checkValidB(form):
  current=[]
  for element in form[0]:
    current.append(element)
  for singleForm in form[1:]:
    tentative=[]
    for element in singleForm:
      if(element in current):
        tentative.append(element)
    current=tentative
  return len(current)

def solve(part):
  rows= getOldAocInput(6)
  declarationForms=buildDeclarationsForm(rows)

  count=0
  for form in declarationForms:
    if(part=="a"):
      count=count+checkValidA(form)
    if(part=="b"):
      count=count+checkValidB(form)
  return count



print(solve("a"))
print(solve("b"))
