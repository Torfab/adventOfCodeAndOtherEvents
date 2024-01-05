from utility import *

def parseRows(rows):
  passports=[]
  currentPassport={}
  for element in rows:
    if(element==""):
      passports.append(currentPassport)
      currentPassport={}
    else:
      rowSplitted=element.split(" ")
      for singleField in rowSplitted:
        singleFieldSplitted=singleField.split(":")
        currentPassport[singleFieldSplitted[0]]=singleFieldSplitted[1]
  passports.append(currentPassport)
  return passports

def isValidPassport(passport, part):
  validFields=["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

  for validField in validFields:
    if (validField not in passport.keys()):
      return 0
  if(part=="a"):
    return 1
  
  if(int(passport["byr"])<1920 or int(passport["byr"])>2002):
    return 0
  
  if(int(passport["iyr"])<2010 or int(passport["iyr"])>2020):
    return 0
  
  if(int(passport["eyr"])<2020 or int(passport["eyr"])>2030):
    return 0
  
  if(passport["hgt"][-2:]!="cm" and passport["hgt"][-2:]!="in"):
    return 0
  if(passport["hgt"][-2:]=="cm" and (int(passport["hgt"][:-2])<150 or int(passport["hgt"][:-2])>193)):
    return 0
  if(passport["hgt"][-2:]=="in" and (int(passport["hgt"][:-2])<59 or int(passport["hgt"][:-2])>76)):
    return 0
  
  validHairColors=["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]
  if(len(passport["hcl"])!=7 or passport["hcl"][0]!="#"):
    return 0
  for element in passport["hcl"][1:]:
    if(element not in validHairColors):
      return 0
    
  validEyeColors=["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
  if(passport["ecl"] not in validEyeColors):
    return 0

  validPid=["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
  if(len(passport["pid"])!=9):
    return 0
  for element in passport["pid"]:
    if (element not in validPid):
      return 0
  return 1

def solve(part):
  
  rows= getOldAocInput(4)
  passports=parseRows(rows)
  count=0
  for passport in passports:
    count=count+isValidPassport(passport, part)
  return count

print(solve("a"))
print(solve("b"))
