from utility import *

fromDectoHex={ 0:'0', 1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9', 10:'a', 11:'b', 12:'c', 13:'d', 14:'e', 15:'f' }
fromHexToDec={ '0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'a':10, 'b':11, 'c':12, 'd':13, 'e':14, 'f':15 }

def findDecimalFromHex(hex):
  value=0
  for idx in reversed(range(len(hex))):
    expOfBase=len(hex)-idx-1
    value= value + fromHexToDec[hex[idx]]*(16**expOfBase)
  return value

def findHexFromDecimal(dec, padding=False):
  result=[]
  while (dec!=0):
    result.append(fromDectoHex[dec%16])
    dec=dec//16
  if(padding and len(result)<2):
    for _ in range(2-len(result)):
      result.append('0')
  result.reverse()
  return ''.join(result)



def buildGridFromRows(rows):
  grid=[]
  for row in rows:
    grid.append(row.split(" "))
  return grid

def solve():
  rows=openFile("input.txt")

  grid=buildGridFromRows(rows)

  for idx, row in enumerate(grid[:-1]):
    value=0
    for element in row[:-1]:
      value=value+findDecimalFromHex(element)
    value=value%256
    checksumComputed=findHexFromDecimal(value, True)
    if(checksumComputed!=row[-1]):
      errorRow=idx
      # print("trovato errore in riga", idx, "valori", findHexFromDecimal(value, True), row[-1])

  for column in range(len(grid[0])-1):
    value=0
    for row in range(len(grid)-1):
      value=value+findDecimalFromHex(grid[row][column])
    value=value%256
    checksumComputed=findHexFromDecimal(value, True)
    if(checksumComputed!=grid[len(grid)-1][column]):
      errorColumn=column
      # print("trovato errore in colonna", column, "valori", findHexFromDecimal(value, True), grid[len(grid)-1][column])
  # print(rows)


  value=0
  for element in grid[errorRow][:-1]:
    value=value+findDecimalFromHex(element)
  value=value%256

  decimalOfError=findDecimalFromHex(grid[errorRow][errorColumn])
  decimalOfChecksum=findDecimalFromHex(grid[errorRow][-1])
  decimalChecksumComputed=value
  difference=(decimalOfChecksum-decimalChecksumComputed)
  correctValue=(decimalOfError+difference)%256

  return(correctValue*decimalOfError)


  # print((decimalOfError-difference)%256)
  # print(findHexFromDecimal((decimalOfError-difference)%256))
  # print((decimalOfChecksum-decimalChecksumComputed)%256)

  # print(grid[errorRow][errorColumn])

  # grid[errorRow][errorColumn]=findHexFromDecimal((decimalOfError+difference)%256)

  # for idx, row in enumerate(grid[:-1]):
  #   value=0
  #   for element in row[:-1]:
  #     value=value+findDecimalFromHex(element)
  #   value=value%256
  #   checksumComputed=findHexFromDecimal(value, True)
  #   if(checksumComputed!=row[-1]):
  #     errorRow=idx
  #     print("trovato errore in riga", idx, "valori", findHexFromDecimal(value, True), row[-1])

  # for column in range(len(grid[0])-1):
  #   value=0
  #   for row in range(len(grid)-1):
  #     value=value+findDecimalFromHex(grid[row][column])
  #   value=value%256
  #   checksumComputed=findHexFromDecimal(value, True)
  #   if(checksumComputed!=grid[len(grid)-1][column]):
  #     errorColumn=column
  #     print("trovato errore in colonna", column, "valori", findHexFromDecimal(value, True), grid[len(grid)-1][column])

  # print("fine")
print(solve())

# print(findHexFromDecimal(255))