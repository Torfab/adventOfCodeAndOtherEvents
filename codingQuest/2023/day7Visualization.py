from utility import *
import curses
from curses import wrapper
import time


moveTuple={'U': (0,-1), 'D': (0,1), 'L':(-1,0), 'R': (1,0)}

def sumTupleValueByValue(a,b):
  # Uso questa funzione per trovare la nuova posizione
  # Aggiunge la tupla di movimenti qui sopra scelta attraverso la mossa e la somma alla testa del serpente
  return a[0]+b[0], a[1]+b[1]

# Stampa comoda della griglia. quella di default non è utile da un punto di vista grafico
def stampaGrid(grid, stdscr):
  for y in range(20):
    for x in range(20):
      if(grid.get((x,y))!=None):
        stdscr.addstr(y,x, grid[(x,y)])
      else:
        stdscr.addstr(y,x, '.')

def checkEatFruit(currentFruit, positionHead):
  return currentFruit==positionHead

def checkLose(position, grid):
  if(position[0]>19 or position[0]<0):
    return True
  if(position[1]>19 or position[1]<0):
    return True
  if(grid.get(position)=="S"):
    return True
  return False

def addScore(score, value):
  return score+value

def buildFruits(fruitsRaw):

  # Il modo che ho deciso di trattare i frutti sono tuple che indicano le posizioni, quindi parto dalla stringa
  # E mi costruisco una lista con queste tuple
  tupleFruits=[]
  for fruit in fruitsRaw:
    splitted=[int(x) for x in fruit.split(",")]
    tupleFruits.append((splitted[0], splitted[1]))
  return tupleFruits

def solve(stdscr):
  stdscr.clear()
  stdscr.addstr(21,0, 'Score')
  rows=openFile("input.txt")
  fruits= buildFruits(rows[1].split(" "))
  moves=[x for x in rows[3]]
  
  # Considero la griglia come un dizionario (tupla: valore)
  # Le tuple sono variabili che contengono DUE valori, nella forma (x,y), e si accedono come nomeVariabile[0], nomeVariabile[1]
  # Se non trovo la tupla vuol dire che quell'elemento dela griglia è vuoto, altrimenti farò si che sia valorizzato
  grid={}

  # snake contiene il corpo del serpente, inizia solo con la testa in posizione (0,0), è una lista di tuple
  snake=[(0,0)]

  # inserisco il corpo del serpente dentro la griglia, da notare che grid è un dizionario
  grid[(0,0)]="S"

  # cursorFruit mi tiene traccia del frutto specifico dove sono arrivato, currentFruit è il valore
  cursorFruit=0
  currentFruit=fruits[cursorFruit]
  grid[currentFruit]="F"

  score=0

  for element in moves:
    # La coda del serpente la devo eliminare, TRANNE SE trovo un frutto.
    # Per non fare confusione nei movimenti nel caso limite in cui mi mangio l'ultimo pezzo della coda
    # Intanto la elimino ma mi conservo la posizione nel caso in cui mi accorgo che trovo un frutto
    temp=snake[0]
    grid.pop(temp)

    #Elimino il primo elemento (fine della coda) e aggiungo un nuovo ultimo elemento (nuova Testa)
    snake.append(sumTupleValueByValue(snake[-1], moveTuple[element]))
    snake.pop(0)
    if(checkLose(snake[-1], grid)):
      # Mi assicuro che il movimento sia legittimo
      break
    score=addScore(score, 1)
    grid[snake[-1]]='S'

    #Ora che so che il movimento è andato a buonfine controllo se la testa si trova esattamente su un frutto e mi comporto di conseguenza
    if(checkEatFruit(currentFruit, snake[-1])):

      score=addScore(score, 100)
      # Devo reinserire la coda
      snake.insert(0, temp)
      grid[temp]='S'

      # Devo considerare un nuovo frutto
      cursorFruit=cursorFruit+1
      currentFruit=fruits[cursorFruit]

      # Questa parte mi serve solo per avere carina la stampa.
      # C'è un piccolo bug di visualizzazione nella stampa per cui se il nuovo frutto è DENTRO il corpo non lo voglio mostrare
      # Quando però il serpente "ESCE" il frutto non appare
      # è facile da sistemare ma ogni ciclo farebbe istruzioni in più senza grosse motivazioni
      # Mi sta bene che non vedo visivamente il frutto in questo caso specifico.
      if(grid.get(currentFruit)==None):
        grid[currentFruit]="F"

    stampaGrid(grid, stdscr) 
    stdscr.addstr(21,6, str(score))
    stdscr.addstr('\n\n')
    stdscr.refresh()
    time.sleep(0.05)
  
  stdscr.addstr(21,0, 'Partita conclusa '+str(score))
  stdscr.addstr(22,0, 'Score finale = '+str(score))
  stdscr.getch()
  return score

def main(stdscr: 'curses._CursesWindow'):
  solve(stdscr)

wrapper(main)