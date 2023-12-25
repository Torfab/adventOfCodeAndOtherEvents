from utility import *

# trivial problem if using external libreries that works on graphs, but where is the fun in that
# my plan started with an assumption: 
# if those 3 bridges exists and i try to navigate the graphs from each node as starting point
# those connections will appears as bottlenecks and will be cross more times than all the others
#
# Infact doing that i found top 3 connections are crossed 20% more than the fourth position
# Being honest i would've expected more but that is that, i removed those connections and valued size of subgraphs


def parseRows(rows):
  grid={}
  for row in rows:
    row=row.split(": ")
    k=row[0]
    if (grid.get(k)==None):
      grid[k]=[]

    for element in row[1].split(" "):
      grid[k].append(element)
      if(grid.get(element)==None):
        grid[element]=[]
      grid[element].append(k)
  return grid

def addCouples(k, grid, couples):
  startNode=k
  border=[]
  for element in grid[k]:
    border.append((k, element))
  marked=set()
  marked.add(startNode)
  while (len(border)>0):
    newBorder=[]
    for element in border:
      if(element[1] in marked):
        continue
      marked.add(element[1])

      if(element[0]<=element[1]):
        el0, el1=element[0], element[1]
      else:
        el1, el0=element[0], element[1]

      if(couples.get((el0, el1))==None):
        couples[(el0, el1)]=1
      else:
        couples[(el0, el1)]=couples[(el0,el1)]+1
      for thingy in grid[element[1]]:
        newBorder.append((element[1], thingy))
    border=newBorder


def top_k_values(dictionary, k):
    sorted_items = sorted(dictionary.items(), key=lambda x: x[1], reverse=True)
    top_k = sorted_items[:k]
    return top_k

def solve():
  rows=getOldAocInput(25)
  grid=parseRows(rows)
  couples={}
  for k in grid.keys():
    addCouples(k, grid, couples)

  topThree = top_k_values(couples, 3)

  for element in topThree:
    grid[element[0][0]].remove(element[0][1])
    grid[element[0][1]].remove(element[0][0])

  k=next(iter(grid))

  border=[k]
  marked=set()
  while(len(border)>0):
    element=border.pop(0)
    marked.add(element)
    for neighbour in grid[element]:
      if(neighbour in marked):
        continue
      border.append(neighbour)
  # print(len(marked))
  # print(len(grid))

  # print(couples)

  return len(marked)*(len(grid)-len(marked))

print(solve())
