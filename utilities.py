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


def getAoCInputGeneric(year, day):
  return aocd.get_data(day=day, year=year).split("\n")


def getAocInput(day):
  return getAoCInputGeneric(date.today().year, day)