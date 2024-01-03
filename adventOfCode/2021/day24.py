from utilityz import getOldAocInput
import functools

@functools.cache
def step(z, inp, firstDiv,firstADD,secondADD):

  z=z//firstDiv

  if(z%26+firstADD==inp):
    return z
  else:
    return z*26+inp+secondADD
  
  #26, -2, 1




def solve(part):
  rows=getOldAocInput(24)
  realSteps=[]
  first=4
  second=5
  third=15

  for _ in range(14):
    realSteps.append((int(rows[first].split(" ")[2]), int(rows[second].split(" ")[2]), int(rows[third].split(" ")[2])))
    first, second, third= first+18, second+18, third+18

  zstack = []
  if(part=="a"):
    inp=list([9]*14)
  if(part=="b"):
    inp=list([1]*14)
  for i, oc in enumerate(realSteps):
    zdiv, xcheck, yadd = oc
    if zdiv == 1:
        zstack.append((i, yadd))
    elif zdiv == 26:
        j, yadd = zstack.pop()
        inp[i] = inp[j] + yadd + xcheck
        if inp[i] > 9:
            inp[j] = inp[j] - (inp[i] - 9)
            inp[i] = 9
        if inp[i] < 1:
            inp[j] = inp[j] + (1 - inp[i])
            inp[i] = 1
  return "".join([str(x) for x in inp])

print(solve("a"))
print(solve("b"))