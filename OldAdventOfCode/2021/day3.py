from utility import *

def convertBinToDec(bin):
  bin=str(bin)
  result=0
  for index in range(len(bin)):
    if(bin[index]=='1'):
      result=result+2**(len(bin)-index-1)
  return result


def solve1():
  rows= getAocInput(3,2021)

  arrayOfPosition=[0]*len(rows[0])

  for element in rows:
    for idx, bit in enumerate(element):
      if(bit=='1'):
        arrayOfPosition[idx]=arrayOfPosition[idx]+1

  gammaRate=''
  epsilonRate=''
  for element in arrayOfPosition:
    if (element>=len(rows)//2):
      gammaRate=gammaRate+'1'
      epsilonRate=epsilonRate+'0'
    else:
      gammaRate=gammaRate+'0'
      epsilonRate=epsilonRate+'1'

  return convertBinToDec(gammaRate)*convertBinToDec(epsilonRate)


def solve2():
  rows= getAocInput(3,2021)

  oxigenGeneratorRating=rows.copy()
  co2ScrubberRating=rows.copy()


  idx=0
  while(len(oxigenGeneratorRating)>1):
    count=0
    for element in oxigenGeneratorRating:
      if(element[idx]=='1'):
        count=count+1
    if(count>=len(oxigenGeneratorRating)/2):
      destroy='0'
    else:
      destroy='1'

    for elementIdx in reversed(range(len(oxigenGeneratorRating))):

      if(oxigenGeneratorRating[elementIdx][idx]==destroy):
        oxigenGeneratorRating.pop(elementIdx)
    idx=idx+1

  idx=0
  while(len(co2ScrubberRating)>1):
    count=0
    for element in co2ScrubberRating:
      if(element[idx]=='1'):
        count=count+1
    if(count>=len(co2ScrubberRating)/2):
      destroy='1'
    else:
      destroy='0'

    for elementIdx in reversed(range(len(co2ScrubberRating))):

      if(co2ScrubberRating[elementIdx][idx]==destroy):
        co2ScrubberRating.pop(elementIdx)
    idx=idx+1

  oxigenGeneratorRating=oxigenGeneratorRating[0]
  co2ScrubberRating=co2ScrubberRating[0]



  return  convertBinToDec(oxigenGeneratorRating)*convertBinToDec(co2ScrubberRating)
  

print(solve1())
print(solve2())