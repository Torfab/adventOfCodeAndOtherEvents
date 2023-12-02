from utility import *

def fromHexToBinary(hex):
  hexDict={
    '0':'0000', '1':'0001', '2':'0010', '3':'0011', '4':'0100', '5':'0101', '6':'0110', '7':'0111', '8':'1000', '9':'1001', 'A':'1010', 'B':'1011', 'C':'1100', 'D':'1101', 'E':'1110', 'F':'1111'
  }
  return hexDict.get(hex)

def fromHexToBinaryLine(hexLine):
  binaryConversion=[]
  for element in hexLine:
    binaryConversion.append(fromHexToBinary(element))
  return ''.join(binaryConversion)


def parseRows(rows):
  grid=[]
  for singleRow in rows:
    newRow=[]
    for singleColumn in singleRow:
      newRow.append(int(singleColumn))
      
    grid.append(newRow)
  return grid

def comprehendPacket(packet, deep, toElaborate, parentTypeID):
  cursor=0
  lenpacket=len(packet)
  elaborated=0
  versionNumberSum=0
  state="VERSION"
  tempResult=[]

  while(cursor<=lenpacket-8):
    if(state=="VERSION"):
      version=packet[cursor:cursor+3]
      versionNumberSum=versionNumberSum+fromBinaryToInteger(version)
      cursor=cursor+3
      state="TYPE_ID"

    if(state=="TYPE_ID"):
      typeID=packet[cursor:cursor+3]
      cursor=cursor+3
      state="VALUE"
    
    if(state=="VALUE"):
      if(typeID=="100"):
        values=[]
        while(packet[cursor]=='1'):
          cursor=cursor+1
          values.append(packet[cursor:cursor+4])
          cursor=cursor+4
        cursor=cursor+1
        values.append(packet[cursor:cursor+4])
        cursor=cursor+4
        singleValue=''.join(values)
        tempResult.append(fromBinaryToInteger(singleValue))

      else:
        lengthID=packet[cursor]
        cursor=cursor+1

        if(lengthID=='0'):
          totalLength=packet[cursor:cursor+15]
          cursor=cursor+15
          intTotalLength=fromBinaryToInteger(totalLength)
          newSumVersion, _, newResult=comprehendPacket(packet[cursor:cursor+intTotalLength], deep+1, -1, typeID)
          tempResult.append(newResult)
          versionNumberSum=versionNumberSum+newSumVersion
          cursor=cursor+intTotalLength

        if(lengthID=='1'):
          totalPackets=packet[cursor:cursor+11]
          cursor=cursor+11
          intTotalPackets=fromBinaryToInteger(totalPackets)
          newSumVersion, newcursor, newResult=comprehendPacket(packet[cursor:], deep+1, intTotalPackets, typeID)
          tempResult.append(newResult)
          versionNumberSum=versionNumberSum+newSumVersion
          cursor=cursor+newcursor
          
      state="VERSION"


    
    elaborated=elaborated+1
    if(elaborated==toElaborate):

      result=findResult(parentTypeID, tempResult)

      return versionNumberSum, cursor, result
      
  result=findResult(parentTypeID, tempResult)

  return versionNumberSum, cursor, result

def findResult(parentTypeID, tempResult):
  if(parentTypeID == '000'):
    result=sum(tempResult)

  elif(parentTypeID == '001'):
    result=1
    for num in tempResult:
      result=result*num

  elif(parentTypeID == '010'):
    result=min(tempResult)

  elif(parentTypeID == '011'):
    result=max(tempResult)

  elif(parentTypeID == '100'):
    result=tempResult[0]

  elif(parentTypeID == '101'):
    if(tempResult[0]>tempResult[1]):
      result=1
    else:
      result=0
  
  elif(parentTypeID == '110'):
    if(tempResult[0]<tempResult[1]):
      result=1
    else:
      result=0

  elif(parentTypeID == '111'):
    if(tempResult[0]==tempResult[1]):
      result=1
    else:
      result=0
  return result

def solve(part):
  rows=getOldAocInput(16)
  code=rows[0]
  code=fromHexToBinaryLine(code)

  result = comprehendPacket(code, 0, -1, '100')
  
  if(part=="a"):
    return result[0]
  if(part=="b"):
    return result[2]




print(solve("a"))
print(solve("b"))