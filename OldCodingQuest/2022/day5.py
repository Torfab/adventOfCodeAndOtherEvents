import hashlib

from utility import *

rows=openFile("input.txt")

def findMined(element, oldHash):
  count=0
  while(True):
    toHash=element+"|"+str(count)+"|"+oldHash
    tentative=hashlib.sha256(toHash.encode('ascii')).hexdigest()
    if (tentative.startswith("000000")):
      print("i've hashed", toHash)
      return str(count), tentative
    count=count+1
    # print(count, tentative)


state="tuttoapposto"

for row in rows:
  splitted=row.split("|")
  scritta=splitted[0]
  if(state=='tuttoapposto'):
    mined=splitted[1]
    oldHash=splitted[2]
    newHash=splitted[3]
    toHash="|".join(splitted[:3])
    # print("i'm hashing", toHash)
    found=hashlib.sha256(toHash.encode('ascii')).hexdigest()
    if(found!=newHash):
      state='Ricostruiamo'
      splitted[1], splitted[3]=findMined(scritta, splitted[2])
      found=splitted[3]
      print("|".join(splitted))
      continue

  if(state=='Ricostruiamo'):
    splitted[2]=found
    splitted[1], splitted[3]=findMined(scritta, splitted[2])
    found=splitted[3]
  # print("|".join(splitted))

print(found)
    
  