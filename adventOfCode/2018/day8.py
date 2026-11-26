from utility import *

def parseRows(rows):
  return [int(x) for x in rows[0].split(" ")]

def evaluateMetadata2(row, cursor=0):
  numChildren=row[cursor]
  cursor=cursor+1
  numMetadata=row[cursor]
  cursor=cursor+1
  children=[]
  for _ in range(numChildren):
    cursor, metaDataValue=evaluateMetadata2(row, cursor)
    children.append(metaDataValue)

  metadataValue=0
  if (numChildren==0):
    for _ in range(numMetadata):
      metadataValue=metadataValue+row[cursor]
      cursor=cursor+1
  else:
    for _ in range(numMetadata):
      index=row[cursor]-1
      if(index<numChildren):
        metadataValue=metadataValue+children[row[cursor]-1]
      cursor=cursor+1
  return cursor, metadataValue


def evaluateMetadata1(row, cursor=0):
  numChildren=row[cursor]
  cursor=cursor+1
  numMetadata=row[cursor]
  cursor=cursor+1
  metadataValue=0
  for _ in range(numChildren):
    result=evaluateMetadata1(row, cursor)
    cursor=result[0]
    metadataValue=metadataValue+result[1]
  for _ in range(numMetadata):
    metadataValue=metadataValue+row[cursor]
    cursor=cursor+1
  return cursor, metadataValue

def solve(part):
  rows=getOldAocInput(8)
  row=parseRows(rows)
  if(part==1):
    return evaluateMetadata1(row)[1]
  else:
    return evaluateMetadata2(row)[1]

print(solve(1))
print(solve(2))