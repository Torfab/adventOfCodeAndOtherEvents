from datetime import date

import aocd


def openFile(path):
  
  file = open(path, "r")
  rows = []
  for line in file:
    rows.append(line.rstrip("\r\n"))
  return rows


def sumArrayValueByValue(a, b):
  return list(map(sum, zip(a, b)))

def multiplyArrayByValue(array, value):
  return [value*a for a in array]

def sumArrayValueByValueSeparated(a, b, c):
  return a+c[0], b+c[0]



def getAocInput(day, year=date.today().year):
  if(day==-1):
    return openFile("test.txt")
  return aocd.get_data(day=day, year=year).split("\n")

def submitToday(answer):
  return aocd.submit(answer)
