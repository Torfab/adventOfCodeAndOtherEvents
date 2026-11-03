from utility import *

directions=fromDistanceBuildSetOfRadialDirections(1)

def parseRows(rows):
  ingredients={}
  for element in rows:
    elementSplitted=element.split(":")
    ingredients[elementSplitted[0]]=elementSplitted[1].split(",")

  return ingredients


def solve1():
  rows=openFile("raw.txt")
  ingredients=parseRows(rows)
  toCheck=set(["NULL"])
  ingredientToNull=set()
  while(len(toCheck)>0):
    newToCheck=set(toCheck)
    for element in newToCheck:
      ingredientToNull.add(element)
      toCheck.discard(element)
      for ingredient in ingredients.get(element, []):
        if ingredient in ingredientToNull:
          continue
        else:
          toCheck.add(ingredient)

  ingredientToNull.discard("NULL")
  return len(ingredientToNull)

def findAllElementdoableWith(IngredientToFind, ingredients):
  toCheck=set()
  surelyDoable=set()
  for ingredient, iList in ingredients.items():
    if IngredientToFind in iList:
      toCheck.add(ingredient)

  while(len(toCheck)>0):
    newToCheck=set(toCheck)
    for checked in newToCheck:
      surelyDoable.add(checked)
      toCheck.discard(checked)
      for ingredient, iList in ingredients.items():
        if checked in iList and ingredient not in surelyDoable:
          toCheck.add(ingredient)
  surelyDoable.discard(IngredientToFind)
  return surelyDoable

def updateOccurrances(occurances, mySet):
  for element in mySet:
    occurances[element]=occurances.get(element,0)+1

def solve2():
  rows=openFile("raw.txt")
  ingredients=parseRows(rows)

  surelyDoable1=findAllElementdoableWith("NULLv1", ingredients)
  surelyDoable2=findAllElementdoableWith("NULLv2", ingredients)
  surelyDoable3=findAllElementdoableWith("NULLv3", ingredients)

  occurances={}
  updateOccurrances(occurances, surelyDoable1)
  updateOccurrances(occurances, surelyDoable2)
  updateOccurrances(occurances, surelyDoable3)

  result=len([x for x,y in occurances.items() if y >=2])
  
  return result
        

print(solve2())
