from utility import *

firstInternal="c0a8"
firstWifi="0A00"


def parseRows(rows):
  newArray=[]
  for row in rows:
    length=row[4:8]
    source=row[24:32]
    receiver=row[32:40]
    newArray.append({"length": length, "source": source, "receiver": receiver})
  return newArray



def solve():
  rows=openFile("input.txt")
  rows=parseRows(rows)
  wifiTraffic=0
  internalTraffic=0

  for element in rows:
    length=fromHexToInteger(element["length"])
    print(element["source"][:4])
    if(element["source"][:4]==firstInternal or element["receiver"][:4]==firstInternal):
      internalTraffic=internalTraffic+length
    if(element["source"][:4]==firstWifi or element["receiver"][:4]==firstWifi):
      print("uh")
      wifiTraffic=wifiTraffic+length
  return str(internalTraffic)+"/"+str(wifiTraffic)
print(solve())