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

def comprehendPacket(packet, deep, toElaborate):
  cursor=0
  lenpacket=len(packet)
  elaborated=0
  versionNumberSum=0
  state="VERSION"

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
      else:
        lengthID=packet[cursor]
        cursor=cursor+1

        if(lengthID=='0'):
          totalLength=packet[cursor:cursor+15]
          cursor=cursor+15
          intTotalLength=fromBinaryToInteger(totalLength)
          # print("dentro", intTotalLength)
          versionNumberSum=versionNumberSum+comprehendPacket(packet[cursor:cursor+intTotalLength], deep+1, -1)
          # print("fuori", cursor, intTotalLength)
          cursor=cursor+intTotalLength
          # print(cursor)

        if(lengthID=='1'):
          totalPackets=packet[cursor:cursor+11]
          cursor=cursor+11
          intTotalPackets=fromBinaryToInteger(totalPackets)
          newSumVersion, newcursor=comprehendPacket(packet[cursor:], deep+1, intTotalPackets)
          versionNumberSum=versionNumberSum+newSumVersion
          cursor=cursor+newcursor
          
      state="VERSION"


    print("version", version, "Type ID", typeID, "values")
    elaborated=elaborated+1
    if(elaborated==toElaborate):
      return versionNumberSum, cursor
      

  return versionNumberSum



def solve():
  rows=getOldAocInput(16)
  code=rows[0]
  code=fromHexToBinaryLine(code)

  # print(code)

  return comprehendPacket(code, 0, -1)

 


print(solve())