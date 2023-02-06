from utility import *

day=19

def comprehension(rows):
  bluePrints=[]
  
  for idx, row in enumerate(rows):
    splitted=row.replace(":", "").replace(".", "").split(" ")
    bluePrint=dict()
    bluePrint["number"]=int(splitted[1])
    bluePrint["oreRobot"]=dict([(splitted[7], int(splitted[6]))])
    bluePrint["clayRobot"]=dict([(splitted[13], int(splitted[12]))])
    bluePrint["obsidianRobot"]=dict([(splitted[19], int(splitted[18])), (splitted[22], int(splitted[21]))])
    bluePrint["geodeRobot"]=dict([(splitted[28], int(splitted[27])), (splitted[31], int(splitted[30]))])
    bluePrints.append(bluePrint)

  return bluePrints

robots=["geodeRobot", "obsidianRobot", "clayRobot", "oreRobot"]
robotYield=dict(geodeRobot="geode", obsidianRobot="obsidian", clayRobot="clay", oreRobot="ore")
maxx=dict()

def findBestRobot(bluePrint, resources, production, maxElements):
  candidateRobots=[]
  for robot in robots:
    if(maxElements[robotYield[robot]]==production[robotYield[robot]]):
      continue
    candidateRobot=bluePrint[robot]
    
    isItALegitCandidate=True
    for resourceType in candidateRobot:
      if (candidateRobot[resourceType]>resources[resourceType]):
        isItALegitCandidate=False
    if(isItALegitCandidate):
      candidateRobots.append(robot)
  return candidateRobots
    
robotProductionType=dict(oreRobot="ore", clayRobot="clay", obsidianRobot="obsidian", geodeRobot="geode")

def calculateProduction(production, resources, bluePrint, minutes, history, nope, maxElements):
  result=0
  if(minutes==0):
    return resources["geode"]
  else:
    robotToBuild=findBestRobot(bluePrint, resources, production, maxElements)
    historyCopy=history.copy()
    if("geodeRobot" in robotToBuild):
      productionCopy=production.copy()
      resourcesCopy=resources.copy()
      productionCopy[robotProductionType["geodeRobot"]]=productionCopy[robotProductionType["geodeRobot"]]+1

      for element in bluePrint["geodeRobot"]:
        resourcesCopy[element]=resourcesCopy[element]-bluePrint["geodeRobot"][element]
      historyCopy=history.copy()
      result=max(calculateProduction(productionCopy, mergeDicts(production, resourcesCopy), bluePrint, minutes-1, historyCopy, [], maxElements), result)
    else:
      candidateRobot= [a for a in robotToBuild if a not in nope]
      for robot in candidateRobot:
        productionCopy=production.copy()
        resourcesCopy=resources.copy()
        productionCopy[robotProductionType[robot]]=productionCopy[robotProductionType[robot]]+1

        for element in bluePrint[robot]:
          resourcesCopy[element]=resourcesCopy[element]-bluePrint[robot][element]
        historyCopy=history.copy()
        result=max(calculateProduction(productionCopy, mergeDicts(production, resourcesCopy), bluePrint, minutes-1, historyCopy, [], maxElements), result)

      result=max(calculateProduction(production.copy(), mergeDicts(production, resources.copy()), bluePrint, minutes-1, historyCopy, robotToBuild, maxElements), result)
        

  return result

def solve1():
  rows=getOldAocInput(day)
  blueprints=comprehension(rows)

  result=0
  for idx, blueprint in enumerate(blueprints):
    maxElements=buildmaxx(blueprint)
    geodes=calculateProduction(dict(ore=1, clay=0, obsidian=0, geode=0), dict(ore=0, clay=0, obsidian=0, geode=0), blueprint, 24, [], [], maxElements)
    result=result+(idx+1)*geodes
  return result

def buildmaxx(blueprint):
  maxElements=dict()
  maxElements["ore"]=max(blueprint["oreRobot"]["ore"], blueprint["clayRobot"]["ore"], blueprint["obsidianRobot"]["ore"], blueprint["geodeRobot"]["ore"])
  maxElements["clay"]=blueprint["obsidianRobot"]["clay"]
  maxElements["obsidian"]=blueprint["geodeRobot"]["obsidian"]
  maxElements["geode"]=9999

  return maxElements

def solve2():
  rows=getOldAocInput(day)
  blueprints=comprehension(rows[:3])

  result=1
  for idx, blueprint in enumerate(blueprints):
    maxElements=buildmaxx(blueprint)
    geodes=calculateProduction(dict(ore=1, clay=0, obsidian=0, geode=0), dict(ore=0, clay=0, obsidian=0, geode=0), blueprint, 32, [], [], maxElements)
    result=result*geodes
  return result

print(solve1())
print(solve2())
