import sys

sys.path.append('..\\..')

def fromIntegerToBinary(integer, padding=16):
  result=[]
  integer=int(integer)

  while (integer!=0):
    result.append(str(integer%2))
    integer=integer//2

  while(len(result)<padding):
    result.append('0')
  result.reverse()
  return ''.join(result)


def fromBinaryToInteger(binary):
  result=0
  power=0
  for element in reversed(range(len(binary))):
    result=result+int(binary[element])*(2**power)
    power=power+1
  return result


from utilities import *