from utility import *

def findLocationRange(seedRange, categories):
  for items in categories.values():
    newSeedRanges=[]
    while(len(seedRange)>0):
      currentLocation=seedRange[0]["start"]
      found=False
      for item in items:
        if(currentLocation>=item["start"] and currentLocation<=item["end"]):
          currentLocation=currentLocation+item["destination"]
          if(seedRange[0]["end"]<=item["end"]):
            newSeedRanges.append({"start":currentLocation, "end": seedRange[0]["end"]+item["destination"]})
          else:
            newSeedRanges.append({"start":currentLocation, "end": item["end"]+item["destination"]})
            seedRange.append({"start": item["end"]+1, "end": seedRange[0]["end"]})
          seedRange.pop(0)
          found=True
          break
      if(found==False):
        newSeedRanges.append(seedRange.pop(0))
    seedRange=newSeedRanges
    newSeedRanges=[]
  return seedRange

def rowsComprehension(rows, part):
  seeds=[]
  oldSeeds=rows[0].split(" ")[1:]
  index=0
  while(index<len(oldSeeds)):
    start=int(oldSeeds[index])
    index=index+1
    if(part=="a"):
      seeds.append({"start":start, "end":start})
      continue
    if(part=="b"):
      end=start+int(oldSeeds[index])-1
      seeds.append({"start":start, "end":end})
      index=index+1
  
  categories={}
  for element in rows[1:]:
    if element=="":
      continue
    if (element[0].isdigit()==False):
      category=element.split(" ")[0]
      categories[category]=[]
      continue
    comprehension=[int(x) for x in element.split(" ")]
    categories[category].append({"destination":comprehension[0]-comprehension[1], "start": comprehension[1], "end": comprehension[1]+comprehension[2]-1})

  return seeds, categories

def solve(part):
  rows=getOldAocInput(5)
  seeds, categories=rowsComprehension(rows, part)
  minimum=None
  for element in seeds:
    start=min([x["start"] for x in findLocationRange([element], categories)])
    if(minimum==None):
      minimum=start
      continue
    minimum=min(start, minimum)
    
  return minimum

print(solve("a"))
print(solve("b"))