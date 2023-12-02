import requests
from utility import *

def fromHexToBinaryLine(hexLine):
  binaryConversion=[]
  for element in hexLine:
    binaryConversion.append(fromHexToBinary(element))
  return ''.join(binaryConversion)


def fromHexToBinary(hex):
  hexDict={
    '0':'0000', '1':'0001', '2':'0010', '3':'0011', '4':'0100', '5':'0101', '6':'0110', '7':'0111', '8':'1000', '9':'1001', 'a':'1010', 'b':'1011', 'c':'1100', 'd':'1101', 'e':'1110', 'f':'1111'
  }
  return hexDict.get(hex)

# print(fromHexToBinaryLine("555500020164048c6df0f53eab92edaf8fbdf0e7c8d597a05ff22cbcc9f17e6e"))

def computeChecksum(message):
  result=0
  cursor=0
  while (cursor<len(message)):
    byte=message[cursor:cursor+8]
    # print('byte', cursor, byte, fromBinaryToInteger(byte))
    result=result+fromBinaryToInteger(byte)
    cursor=cursor+8
  return result

def computeAsciiFromBinary(message):
  asciiDict = {i: chr(i) for i in range(128)}
  cursor=0
  result=[]
  while cursor<len(message):
    binaryElement=message[cursor:cursor+8]
    result.append(asciiDict[fromBinaryToInteger(binaryElement)])
    cursor=cursor+8

  return ''.join(result)

def solve():
  response = requests.get("https://codingquest.io/api/puzzledata?puzzle=21")
  rows = response.text.splitlines()

  fullMessage={}

  for row in rows:
    binaryRow=fromHexToBinaryLine(row)
    if(binaryRow[0:16]!=('0101010101010101')):
      continue

    senderNumber=binaryRow[16:48]
    sequenceNumber=binaryRow[48:56]
    checkSum=binaryRow[56:64]
    message=binaryRow[64:256]
    integerCheckSum=fromBinaryToInteger(checkSum)

    computedChecksum=computeChecksum(message)%256

    if(integerCheckSum!=computedChecksum):
      # print(integerCheckSum, 'diverso da ', computedChecksum)
      continue

    integerSequenceNumber=fromBinaryToInteger(sequenceNumber)
    if(fullMessage.get(integerSequenceNumber)==None):
      fullMessage[integerSequenceNumber]=''
    else:
      print("oh no, errore")

    fullMessage[integerSequenceNumber]=fullMessage[integerSequenceNumber]+message

    
  arrayOfKeys=list(fullMessage.keys())
  arrayOfKeys.sort()
  message=[]
  for element in arrayOfKeys:
    message.append(fullMessage[element])
  messageBinary=''.join(message)
  return computeAsciiFromBinary(messageBinary)

print(solve())
