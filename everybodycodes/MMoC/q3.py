from utilityz import *

def evaluateTree(tree, cursor):
  result=0
  if tree["leftNode"]:
    subresult,cursor=evaluateTree(tree["leftNode"], cursor)
    result=result+subresult
  result=result+cursor*tree["id"]
  cursor=cursor+1
  if tree["rightNode"]:
    subresult, cursor=evaluateTree(tree["rightNode"], cursor)
    result=result+subresult
  return result, cursor
  

def updatetree1(tree, element):
  plug=element["plug"]
  if tree["leftNode"]:
    if(updatetree1(tree["leftNode"], element)):
      return True
  else:
    if tree["leftSocket"]==plug:
      tree["leftNode"]=element
      return True
  if tree["rightNode"]:
    if(updatetree1(tree["rightNode"], element)):
      return True
  else:
    if tree["rightSocket"]==plug:
      tree["rightNode"]=element
      return True
  return False

def updatetree2(tree, element):
  plugShape, plugColor=element["plug"].split(" ")
  if tree["leftNode"]:
    if(updatetree2(tree["leftNode"], element)):
      return True
  else:
    socketShape, socketColor=tree["leftSocket"].split(" ")
    if socketShape==plugShape or socketColor==plugColor:
      tree["leftNode"]=element
      return True
  if tree["rightNode"]:
    if(updatetree2(tree["rightNode"], element)):
      return True
  else:
    socketShape, socketColor=tree["rightSocket"].split(" ")
    if socketShape==plugShape or socketColor==plugColor:
      tree["rightNode"]=element
      return True
  return False

def updatetree3(tree, element):
  if tree["leftNode"]:
    if tree["leftType"]=="strong":
      element=(updatetree3(tree["leftNode"], element))
      if element==None:
        return None
    elif tree["leftType"]=="weak":
      if tree["leftSocket"]==element["plug"]:
        tree["leftType"]="strong"
        newElement=tree["leftNode"]
        tree["leftNode"]=element
        element=newElement
      else:
        element=(updatetree3(tree["leftNode"], element))
        if element==None:
          return None
  else:
    if tree["leftSocket"]==element["plug"]:
      tree["leftType"]="strong"
      tree["leftNode"]=element
      return None
    socketShape, socketColor=tree["leftSocket"].split(" ")
    plugShape, plugColor=element["plug"].split(" ")
    if socketShape==plugShape or socketColor==plugColor:
      tree["leftType"]="weak"
      tree["leftNode"]=element
      return None

  if tree["rightNode"]:
    if tree["rightType"]=="strong":
      element=(updatetree3(tree["rightNode"], element))
      if element==None:
        return None
    elif tree["rightType"]=="weak":
      if tree["rightSocket"]==element["plug"]:
        tree["rightType"]="strong"
        newElement=tree["rightNode"]
        tree["rightNode"]=element
        element=newElement
      else:
        element=(updatetree3(tree["rightNode"], element))
        if element==None:
          return None
  else:
    if tree["rightSocket"]==element["plug"]:
      tree["rightType"]="strong"
      tree["rightNode"]=element
      return None
    socketShape, socketColor=tree["rightSocket"].split(" ")
    plugShape, plugColor=element["plug"].split(" ")
    if socketShape==plugShape or socketColor==plugColor:
      tree["rightType"]="weak"
      tree["rightNode"]=element
      return None
  return element



def parseRows(rows, part):
  items=[]
  for element in rows:
    elementSplitted=element.split(", ")
    singleItem={}
    for innerElement in elementSplitted:
      innerElementSplitted=innerElement.split("=")
      if innerElementSplitted[0]=="id":
        singleItem[innerElementSplitted[0]]=int(innerElementSplitted[1])
      else:
        singleItem[innerElementSplitted[0]]=innerElementSplitted[1]
      singleItem["leftNode"]=None
      singleItem["leftType"]=None
      singleItem["rightNode"]=None
      singleItem["RightType"]=None
    items.append(singleItem)

  tree=items[0]
  for element in items[1:]:
    if part==1:
      if(not updatetree1(tree, element)):
        print("oh no")
    if part==2:
      if(not updatetree2(tree, element)):
        print("oh no")
    if part==3:
      updated=updatetree3(tree, element)
      while(updated!=None):
        updated=updatetree3(tree, updated)


  return tree

def solve(part):
  rows=openFile("raw.txt")
  tree=parseRows(rows, part)
  return evaluateTree(tree, 1)[0]


print(solve(3))