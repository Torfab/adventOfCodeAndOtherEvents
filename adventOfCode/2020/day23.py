from utility import *

def parseRows(rows):
  row=rows[0]
  fastDict={}
  for idx in range(len(row)-1):
    fastDict[int(row[idx])]=int(row[idx+1])

  return fastDict, int(row[-1]), int(row[0])

def solve(part):
  rows=getOldAocInput(23)
  cups, lastElement, firstElement=parseRows(rows)

  if part=="a":
    numElements=max(cups.keys())
    numIterations=100
    finalElement=lastElement

  if part=="b":
    cups[lastElement]=10
    numElements=1_000_000
    numIterations=10_000_000
    finalElement=numElements

  for i in range(10, numElements+1):
    cups[i]=i+1
  cups[finalElement]=firstElement

  currentElement=firstElement

  for i in range(numIterations):
    firstElement=cups[currentElement]
    secondElement=cups[firstElement]
    thirdElement=cups[secondElement]
    destination=(currentElement-2)%numElements+1
    while(destination==firstElement or destination==secondElement or destination==thirdElement):
      destination=(destination-2)%numElements+1
    # Aggancio l'elemento attuale con il primo elemento non preso
    cups[currentElement]=cups[thirdElement]
    #Aggancio l'ultimo elemento all'elemento successivo a quello preso
    cups[thirdElement]=cups[destination]
    #Aggancio la destinazione al primo elementro preso
    cups[destination]=firstElement

    #cambio l'elemento attuale per il prossimo turno
    currentElement=cups[currentElement]
  if part=="a":
    ris=""
    currentElement=cups[1]
    while(currentElement!=1):
      ris=ris+str(currentElement)
      currentElement=cups[currentElement]
    return ris
  if part=="b":
    return cups[1]*cups[cups[1]]

print(solve("a"))
print(solve("b"))