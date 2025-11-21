from utility import *

def parseRows(rows):
  wheel=[1]
  count=1
  direction="R"
  for row in rows:
    if(direction=="R"):
      wheel.insert(-count, int(row))
      direction="L"
    elif(direction=="L"):
      wheel.insert(count, int(row))
      direction="R"
      count=count+1
  
  return [wheel[-1]]+wheel[:-1]

def parseRows2(rows):
  wheel=['1-1']
  count=1
  direction="R"
  elements=1
  for row in rows:
    a,b=row.split("-")
    elements=elements+int(b)-int(a)+1
    if(direction=="R"):
      wheel.insert(-count, row)
      direction="L"
    elif(direction=="L"):
      wheel.insert(count, b+'-'+a)
      direction="R"
      count=count+1
  
  return [wheel[-1]]+wheel[:-1], elements


def solve():
  rows=openFile("raw.txt")
  wheel=parseRows(rows)


  return wheel[2025%len(wheel)]

def solve2():
  rows=openFile("raw.txt")
  wheel, elements=parseRows2(rows)


  # return wheel[2025%len(wheel)]
  found=202520252025%elements

  for nums in wheel[1:]:
    a,b=[int(x) for x in nums.split("-")]
    myRange=max(a,b)-min(a,b)+1
    if found>myRange:
      found=found-myRange
    else:
      if a<b:
        return a+found-1
      if b<a:
        return a-found+1
  


# print(solve("a"))
# print(solve("b"))
print(solve2())
