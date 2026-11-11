from utility import *

def parseRows(rows):
  return rows[0]

def generateAlphabet():
  alphabet={}
  letters="abcdefghijklmnopqrstuvwxyz"
  for letter in letters:
    capitalized=letter.upper()
    alphabet[letter]=capitalized
    alphabet[capitalized]=letter
  return alphabet

#Nave implementation
def oldReducePolymer(polymer, alphabet):
  newPolymer=[]
  while(polymer!=newPolymer):
    newPolymer=list(polymer)
    cursor=len(polymer)-1
    while(cursor>0):
      letter=polymer[cursor]
      backwordLetter=polymer[cursor-1]
      if(letter==alphabet[backwordLetter]):
        polymer.pop(cursor)
        polymer.pop(cursor-1)
        cursor=cursor-2
        
      else:
        cursor=cursor-1
  # return polymer
  return polymer

def reducePolymer(polymer, alphabet):
  stack = []
  for unit in polymer:
    if stack and stack[-1] == alphabet[unit]:
      stack.pop()
    else:
      stack.append(unit)
  return stack

def solve(part):
  rows= openFile("raw.txt")
  polymer=[x for x in parseRows(rows)]
  alphabet=generateAlphabet()

  if(part==1):
    polymer=reducePolymer(polymer, alphabet)
  else:
    minPolymer=False
    minLenPolymer=float("inf")
    
    for letter in "abcdefghijklmnopqrstuvwxyz":
      tempPolymer=[x for x in polymer if x!=letter and x!=letter.upper()]
      tempPolymer=reducePolymer(tempPolymer, alphabet)
      if(len(tempPolymer)<minLenPolymer):
        minLenPolymer=len(tempPolymer)
        minPolymer=tempPolymer

    polymer=minPolymer
  return len(polymer)

# print(solve(1))
evaluateTime(solve,2)