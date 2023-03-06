from enum import Enum

from utility import *


class SceltaAvversario(Enum):
  ROCK='A'
  PAPER='B'
  SCISSOR='C'

class SceltaMia(Enum):
  ROCK='X'
  PAPER='Y'
  SCISSOR='Z'

class TipoScelta(Enum):
  SCONFITTA='X'
  PAREGGIO='Y'
  VITTORIA='Z'

dizionarioPunteggi= dict(X=1, Y=2, Z=3)

def round1(a,b):
  if (a==SceltaAvversario.PAPER.value):
    if(b==SceltaMia.PAPER.value):
      return 3
    if(b==SceltaMia.SCISSOR.value):
      return 6
  if (a==SceltaAvversario.ROCK.value):
    if(b==SceltaMia.ROCK.value):
      return 3
    if(b==SceltaMia.PAPER.value):
      return 6
  if(a==SceltaAvversario.SCISSOR.value):
    if(b==SceltaMia.SCISSOR.value):
      return 3
    if(b==SceltaMia.ROCK.value):
      return 6
  return 0

def round2(b,a):
  if (a==TipoScelta.SCONFITTA.value):
    if(b==SceltaAvversario.PAPER.value):
      return SceltaMia.ROCK.value
    if(b==SceltaAvversario.SCISSOR.value):
      return SceltaMia.PAPER.value
    if(b==SceltaAvversario.ROCK.value):
      return SceltaMia.SCISSOR.value
  if (a==TipoScelta.VITTORIA.value):
    if(b==SceltaAvversario.PAPER.value):
      return SceltaMia.SCISSOR.value
    if(b==SceltaAvversario.SCISSOR.value):
      return SceltaMia.ROCK.value
    if(b==SceltaAvversario.ROCK.value):
      return SceltaMia.PAPER.value
  if (a==TipoScelta.PAREGGIO.value):
    if(b==SceltaAvversario.PAPER.value):
      return SceltaMia.PAPER.value
    if(b==SceltaAvversario.SCISSOR.value):
      return SceltaMia.SCISSOR.value
    if(b==SceltaAvversario.ROCK.value):
      return SceltaMia.ROCK.value

  return 'absurd'


def solve1():
  
  rows= getOldAocInput(2)

  accumulatore=0

  for element in rows:
    splitted = element.split(" ")
    sceltaAvversario = splitted[0]
    sceltaMia = splitted[1]

    accumulatore = accumulatore + round1(sceltaAvversario, sceltaMia) + dizionarioPunteggi[sceltaMia]
    
  return accumulatore

def solve2():

  rows = getOldAocInput(2)

  accumulatore = 0

  for element in rows:
    splitted = element.split(" ")
    sceltaAvversario = splitted[0]
    sceltaMia = splitted[1]

    sceltaMiaDavvero=round2(sceltaAvversario, sceltaMia)
    accumulatore = accumulatore + round1(sceltaAvversario, sceltaMiaDavvero) + dizionarioPunteggi[sceltaMiaDavvero]
    
  return accumulatore

print(solve1())
print(solve2())


