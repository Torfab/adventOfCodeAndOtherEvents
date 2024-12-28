from utility import *

def parseRows(rows):
  bucket={}
  parsedRows=[]
  for row in rows:
    row=row.replace(",", "")
    firstPar=row.find("(")
    ingredients=set(row[:firstPar-1].split(" "))
    for ingredient in ingredients:
      bucket[ingredient]=bucket.get(ingredient, 0)+1
    allergens=row[firstPar+1:-1].split(" ")
    parsedRows.append((ingredients, allergens[1:]))
  return bucket, parsedRows

def checkAndUpdateIfSolution(candidateAllergens, englishAllergen, allergens, allergenKeys):
  if len(candidateAllergens[englishAllergen])==1:
    foreignAllergen=list(candidateAllergens[englishAllergen])[0]
    allergens[foreignAllergen]=englishAllergen
    allergenKeys.add(foreignAllergen)
    removeFromCandidates(candidateAllergens, englishAllergen, foreignAllergen, allergens, allergenKeys)

def removeFromCandidates(candidateAllergens, englishAllergen, foreignAllergen, allergens, allergenKeys):
  for k,v in candidateAllergens.items():
    if k==englishAllergen:
      continue
    if(len(v)==1):
      continue
    v.discard(foreignAllergen)
    checkAndUpdateIfSolution(candidateAllergens, k, allergens, allergenKeys)

def solve(part):
  rows=getOldAocInput(21)
  bucket, parsedRows=parseRows(rows)
  allergens={}
  allergenKeys=set()
  candidateAllergens={}
  for ingredients, englishAllergens in parsedRows:
    for englishAllergen in englishAllergens:
      if candidateAllergens.get(englishAllergen)==None:
        candidateAllergens[englishAllergen]=ingredients-allergenKeys
        checkAndUpdateIfSolution(candidateAllergens, englishAllergen, allergens, allergenKeys)
      else:
        candidateAllergens[englishAllergen]=(ingredients-allergenKeys).intersection(candidateAllergens[englishAllergen])
        checkAndUpdateIfSolution(candidateAllergens, englishAllergen, allergens, allergenKeys)
  
  if part=="a":
    allergens=set(allergens.keys())
    ris=0
    for element, v in bucket.items():
      if element not in allergens:
        ris=ris+v
    return ris
  if part=="b":
    allergens={v:k for k,v in allergens.items()}
    allergensList=list(allergens.keys())
    allergensList.sort()
    foreignAllergenList=[]
    for k in allergensList:
      foreignAllergenList.append(allergens[k])
    return ",".join(foreignAllergenList)

print(solve("a"))
print(solve("b"))
# print(solveB())

# def timeElapse():
#   print(solve())
#   print(solveB())

# print(evaluateTime(timeElapse))
