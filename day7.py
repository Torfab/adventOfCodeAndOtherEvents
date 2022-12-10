from utilities import *


def comprehension(rows):

  root=dict()
  stack=[]
  pointer=root
  size=0

  doublecheck=0

  for element in rows:
    elementSplitted=element.split(" ")
    if(elementSplitted[0]=="$"):
      if(elementSplitted[1]=="ls"):
        continue
      if(elementSplitted[2]=='..'):
        size=pointer["size"]
        pointer=root
        stack.pop()
        for stackElement in stack:
          pointer=next(a for a in pointer["elements"] if a["name"]==stackElement)
        pointer["size"]=pointer["size"]+size

      elif(elementSplitted[2]=="/"): #assumo che esista solo una cartella chiamata /
        pointer=root
        pointer["type"]="dir"
        pointer["name"]=elementSplitted[2]
        pointer["size"]=0
        pointer["elements"]=[]
      else:
        pointer=next(a for a in pointer["elements"] if a["name"]==elementSplitted[2])
        stack.append(elementSplitted[2])

    elif(elementSplitted[0]=='dir'):
      pointer["elements"].append(dict(type="dir", name=elementSplitted[1], size=0, elements=[]))
    else:
      pointer["elements"].append(dict(type="file", name=elementSplitted[1], size=int(elementSplitted[0])))
      pointer["size"]=pointer["size"]+int(elementSplitted[0])
      doublecheck=doublecheck+int(elementSplitted[0])
  while(len(stack)>0):
    size=pointer["size"]
    stack.pop()
    pointer=root
    for stackElement in stack:
      pointer=next(a for a in pointer["elements"] if a["name"]==stackElement)
    pointer["size"]=pointer["size"]+size

  return root

def buildSizes(fileSystem):
  sizes=[]
  buildSizesInnerRecursion(fileSystem, sizes)
  return sizes

def buildSizesInnerRecursion(fileSystem, sizes:list):
  if(fileSystem["type"]=="dir"):
    sizes.append(fileSystem["size"])
  if (fileSystem.get("elements")!=None):
    for element in fileSystem["elements"]:
      buildSizesInnerRecursion(element, sizes)

def solve1():
  rows=getAocInput(7)
  fileSystem=comprehension(rows)
  sizes=buildSizes(fileSystem)

  return sum(element for element in sizes if element<=100000)

def solve2():
  rows=getAocInput(7)
  fileSystem=comprehension(rows)
  sizes=buildSizes(fileSystem)

  spaceToFree=fileSystem["size"]-40000000
  
  return min([element for element in sizes if element>=spaceToFree])

print(solve1())
print(solve2())