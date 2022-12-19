from utilities import *


day=-1

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

def findBestRobot(bluePrint, resources):
  for robot in robots:
    candidateRobot=bluePrint[robot]
    flag=True
    for resourceType in candidateRobot:
      if (candidateRobot[resourceType]>resources[resourceType]):
        flag=False
    if(flag):
      return robot
  return "None"
    
robotProductionType=dict(oreRobot="ore", clayRobot="clay", obsidianRobot="obsidian", geodeRobot="geode")

def calculateProduction(production, resources, bluePrint, minutes, history):
  result=0
  if(minutes==0):
    if(resources["geode"]==10):
      print(history)
    return resources["geode"]
  else:
    robotToBuild=findBestRobot(bluePrint, resources)
    historyCopyZero=history.copy()
    historyCopyZero.append(dict(minutes=25-minutes, robot="None", resources=resources))
    if(robotToBuild=="None"):
      result=max(calculateProduction(production.copy(), mergeDicts(production, resources), bluePrint, minutes-1, historyCopyZero), result)
    else:
      productionCopy=production.copy()
      resourcesCopy=resources.copy()
      productionCopy[robotProductionType[robotToBuild]]=productionCopy[robotProductionType[robotToBuild]]+1

      for element in bluePrint[robotToBuild]:
        resourcesCopy[element]=resourcesCopy[element]-bluePrint[robotToBuild][element]
      historyCopy=history.copy()
      historyCopy.append(dict(minutes=25-minutes, robot=robotToBuild, resources=resources, newResources=resourcesCopy))
      result=max(calculateProduction(productionCopy, mergeDicts(production, resourcesCopy), bluePrint, minutes-1, historyCopy), result)
      if(robotToBuild!="geodeRobot"):
        result=max(calculateProduction(production.copy(), mergeDicts(production, resources), bluePrint, minutes-1, historyCopyZero), result)

  return result

def solve():
  rows=getAocInput(day)
  blueprints=comprehension(rows)

  for blueprint in blueprints:
    print(blueprint)
    geodes=calculateProduction(dict(ore=1, clay=0, obsidian=0, geode=0), dict(ore=0, clay=0, obsidian=0, geode=0), blueprint, 24, [])
    print("num", geodes)

  return None


print(solve())
