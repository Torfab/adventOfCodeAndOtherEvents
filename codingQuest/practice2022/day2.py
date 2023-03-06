from utility import *

rows=openFile("input.txt")

def isValid(word: str):

  if(word[6]!='s'):
    return False
  if(word[1]!='o'):
    return False
  if(word[2]!='o'):
    return False
  if(word[4]!='i'):
    return False

  if(word[0]=='k'):
    return False
  if(word[1]=='e'):
    return False
  if(word[4]=='e'):
    return False
  if(word[5]=='s'):
    return False
  if(word[0]=='s'):
    return False
  if(word[2]=='c'):
    return False
  if(word[3]=='i'):
    return False
  if(word[4]=='e'):
    return False
  
  whiteListElements=['k','e','s','o','c','i']

  for element in whiteListElements:
    if(element not in word):
      return False

  banListElements=['y', 'l', 't', 'p', 'h', 'b', 'a']
  for element in banListElements:
    if(element in word):
      return False
  return True

def solve():

  for element in rows:
    if(isValid(element)):
      return element

print(solve())