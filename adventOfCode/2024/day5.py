from utility import *

def parseRows(rows):
  rulesToHaveFirst={}
  books=[]
  state=0
  for row in rows:
    if state==0:
      if row=="":
        state=1
        continue
      else:
        splittedRow=row.split("|")
        if(rulesToHaveFirst.get(int(splittedRow[1]))==None):
          rulesToHaveFirst[int(splittedRow[1])]=set()

        rulesToHaveFirst[int(splittedRow[1])].add(int(splittedRow[0]))

    if state==1:
      books.append([int(x) for x in row.split(",")])
  return rulesToHaveFirst, books
    


def isGoodBook(book, rules):
  for i in range(len(book)-1):
    current=book[i]
    if (rules.get(current)!=None):
      for element in rules[current]:
        if element in book[i+1:]:
          return False
  return True
def evaluateGoodBook(book, rules):
  if(isGoodBook(book, rules)):
    return  book[len(book)//2]
  return 0

def sortBook(book, rules):
  currentBook=book.copy() # Not necessary but i don't want to have collateral effect from function
  result=[]
  while(len(currentBook)>0): # I will remove element from that copy one by one until it's empty
    for idx in range(len(currentBook)):
      if rules.get(currentBook[idx])==None: 
        result.append(currentBook.pop(idx))
        break
      if(thingInCommonArray(currentBook, rules[currentBook[idx]])):
        continue
      result.append(currentBook.pop(idx))
      break
  return result


def evaluateBadBook(book, rules):
  if(isGoodBook(book, rules)):
    return 0
  book=sortBook(book, rules)
  return book[len(book)//2]

def solve(f):
  rows=getOldAocInput(5)
  rules, books=parseRows(rows)
  ris=0
  for book in books:
    ris=ris+f(book, rules)

  return ris


print(solve(evaluateGoodBook))
print(solve(evaluateBadBook))

