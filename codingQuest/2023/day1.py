from utility import *

def solve():

  rows= openFile("input.txt")

  results={}

  for row in rows:
    splitted=row.split(" ")

    value=int(splitted[1])
    category=splitted[2]

    # Creo una entry nel dizionario se non esiste, altrimenti aggiungo il valore corrente a quello passato
    if(results.get(category)==None):
      results[category]=int(value)
    else:
      results[category]=results[category]+int(value)

  risultato=1
  for element in results.values():
    risultato=risultato*(element%100)
    
  print(risultato)

solve()