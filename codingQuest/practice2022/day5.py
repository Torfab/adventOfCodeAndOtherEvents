from utility import *

hexToBin= {
  '0':'0000',
  '1':'0001',
  '2':'0010',
  '3':'0011',
  '4':'0100',
  '5':'0101',
  '6':'0110',
  '7':'0111',
  '8':'1000',
  '9':'1001',
  'a':'1010',
  'b':'1011',
  'c':'1100',
  'd':'1101',
  'e':'1110',
  'f':'1111'
}

binToStr= {
  '0010':"A",
  '0000':"E",
  '0001':"T",
  '0011':"I",
  '0100':"N",
  '0101':"O",
  '0110':"S",
  '0111':"H",
  '10000':"R",
  '10001':"D",
  '10010':"L",
  '10011':"U",
  '10100':"C",
  '10101':"M",
  '10110':"F",
  '10111':"B",
  '1100000':"F",
  '1100001':"Y",
  '1100010':"W",
  '1100011':"G",
  '1100100':"P",
  '1100101':"B",
  '1100110':"V",
  '1100111':"K",
  '1101000':"Q",
  '1101001':"J",
  '1101010':"X",
  '1101011':"Z",
  '1110000':"0",
  '1110001':"1",
  '1110010':"2",
  '1110011':"3",
  '1110100':"4",
  '1110101':"5",
  '1110110':"6",
  '1110111':"7",
  '1111000':"8",
  '1111001':"9",
  '1111010':"_",
  '1111011':".",
  '1111100':"'",
  '1111111':"*"
}

def decodeHexToBin(hexStr):
  result=[]
  for element in hexStr:
    result.append(hexToBin[element])
  return ''.join(result)

def decodebinToStr(binStr:str):
  cursor=0
  result=[]
  while(cursor<len(binStr)):
    if(binStr[cursor]=='0'):
      # print(binStr[cursor:cursor+4])
      result.append(binToStr[binStr[cursor:cursor+4]])
      cursor=cursor+4
      continue
    if(binStr[cursor]=='1'):
      if(binStr[cursor+1]=='0'):
        # print(binStr[cursor:cursor+5])
        result.append(binToStr[binStr[cursor:cursor+5]])
        cursor=cursor+5
        continue
      else:
        # print(binStr[cursor:cursor+7])
        element=binToStr[binStr[cursor:cursor+7]]
        if(element=='*'):
          break
        result.append(element)
        cursor=cursor+7
        continue
    print(result[-1], end='')
  return ''.join(result)

def solve():
  rows=openFile("input.txt")
  hexStr=rows[0]
  return decodebinToStr(decodeHexToBin(hexStr))

print(solve())