from utility import *

rows= openFile("input.txt")

results={}

for row in rows:
  splitted=row.split(" ")

  if(results.get(splitted[2])==None):
    results[splitted[2]]=int(splitted[1])
  else:
    results[splitted[2]]=results[splitted[2]]+int(splitted[1])

risultato=1
for element in results.values():
  risultato=risultato*(element%100)
  
  
print(risultato)