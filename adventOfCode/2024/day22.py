from utility import *

def solve():
  rows=getOldAocInput(22)
  ris=0
  for row in rows:
    secret=int(row)
    for _ in range(2000):
      secret=secret*64^secret
      secret=secret%16777216

      secret=secret//32^secret
      secret=secret%16777216

      secret=secret*2048^secret
      secret=secret%16777216

    ris=ris+secret
  return ris

def solveB():
  rows=getOldAocInput(22)
  arrayOfSequencesToBanana=[]
  possibleSequences=set()
  for row in rows:
    secret=int(row)
    singleSequencesToBanana={}
    arrayOfSubResult=[]
    oldLastDigit=secret%10
    singlePossibleSequence=set()
    for _ in range(4):
      secret=secret*64^secret
      secret=secret%16777216

      secret=secret//32^secret
      secret=secret%16777216

      secret=secret*2048^secret
      secret=secret%16777216
      arrayOfSubResult.append(secret%10-oldLastDigit)
      oldLastDigit=secret%10
    sequence=tuple(arrayOfSubResult)
    singleSequencesToBanana[tuple(arrayOfSubResult)]=oldLastDigit
    singlePossibleSequence.add(sequence)
    for _ in range(1996):
      secret=secret*64^secret
      secret=secret%16777216

      secret=secret//32^secret
      secret=secret%16777216

      secret=secret*2048^secret
      secret=secret%16777216

      arrayOfSubResult.pop(0)
      arrayOfSubResult.append(secret%10-oldLastDigit)
      oldLastDigit=secret%10
      sequence=tuple(arrayOfSubResult)
      if sequence not in singlePossibleSequence:
        singleSequencesToBanana[sequence]=oldLastDigit
        singlePossibleSequence.add(sequence)
    possibleSequences=possibleSequences.union(singlePossibleSequence)
    arrayOfSequencesToBanana.append(singleSequencesToBanana)
  maxRis=0
  for sequence in possibleSequences:
    tempRis=0
    for singleThingyThongy in arrayOfSequencesToBanana:
      tempRis=tempRis+singleThingyThongy.get(sequence,0)
    maxRis=max(tempRis, maxRis)
  return maxRis

print(solveB())
print(solveB())

# def timeElapse():
#   print(solve())
#   print(solveB())

# print(evaluateTime(timeElapse))

