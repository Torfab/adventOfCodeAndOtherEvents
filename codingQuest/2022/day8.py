from utility import *

rows=openFile("input.txt")

def decode(characterSet, secretKey, message):
  cursorKey=0
  for element in message:
    movement=characterSet.index(secretKey[cursorKey])
    index=characterSet.index(element)
    index=(index-movement-1)%len(characterSet)
    print(characterSet[index], end="")
    cursorKey=(cursorKey+1)%len(secretKey)

characterSet="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.,;:?! '()"
secretKey="Roads? Where We're Going, We Don't Need Roads."

decode(characterSet, secretKey, rows[0])
