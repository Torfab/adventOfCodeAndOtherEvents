from datetime import date

import aocd


def openFile(path):
  file = open(path, "r")
  rows = []
  i = 0
  while True:
    row = file.readline().strip()
    if not row:
      break
    rows.append(row)
    i += 1
  return rows


def sumArrayValueByValue(a, b):
  return list(map(sum, zip(a, b)))

def sumArrayValueByValueSeparated(a, b, c):
  return a+c[0], b+c[0]



def getAoCInputGeneric(year, day):
  return aocd.get_data(day=day, year=year).split("\n")


def getAocInput(day):
  if(day==-1):
    return openFile("test.txt")
  return getAoCInputGeneric(date.today().year, day)