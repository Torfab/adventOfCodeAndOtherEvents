from utilityz import *

def parseRows(rows):
  width=int(rows[0].split("=")[1])
  height=int(rows[1].split("=")[1])
  widthCommands=rows[2].split("=")[1]
  heightCommands=rows[3].split("=")[1]
  
  return  width, height, widthCommands, heightCommands

def buildRealCommands(commands):
  realCommands=[]
  current=int(commands[0])
  even=0
  for selement in commands[1:]:
    element=int(selement)
    if element==current:
      realCommands.append((element,element==even))
    else:
      current=element
      realCommands.append((element,None))
    even=(even+1)%2
  return realCommands

def buildTrulyCommands(commands):
  realCommands=[]
  current=commands[0]
  for selement in commands[1:]:
    element=int(selement)
    if element==current:
      if(element==0):
        realCommands.append((element,True))
      else:
        realCommands.append((element,False))
    else:
      current=element
      realCommands.append((element,None))
  return realCommands

def solve():
  rows=openFile("raw.txt")
  width, height, widthCommands, heightCommands=parseRows(rows)
  widthCommands=widthCommands*(height//len(widthCommands)+1)
  heightCommands=heightCommands*(width//len(heightCommands)+1)
  widthCommands=widthCommands[:height+1]
  heightCommands=heightCommands[:width+1]
  realWidthCommands=buildRealCommands(widthCommands)
  realHeightCommands=buildRealCommands(heightCommands)

  result=0
  result=realWidthCommands.count((1,False))*realHeightCommands.count((0,False))
  result=result+realWidthCommands.count((0,False))*realHeightCommands.count((1,False))
  result=result+realWidthCommands.count((0,True))*realHeightCommands.count((0,True))
  result=result+realWidthCommands.count((1,True))*realHeightCommands.count((1,True))

  
  return result

def solve2():
  rows=openFile("raw.txt")
  width, height, widthCommands, heightCommands=parseRows(rows)
  widthCommands=widthCommands*(height//len(widthCommands)+1)
  heightCommands=heightCommands*(width//len(heightCommands)+1)
  widthCommands=widthCommands[:height+1]
  heightCommands=heightCommands[:width+1]
  realWidthCommands=buildTrulyCommands(widthCommands)
  realHeightCommands=buildTrulyCommands(heightCommands)

  
  startColor=int(widthCommands[0])

  currentX=int(heightCommands[0])
  currentY=int(widthCommands[0])

  stepX=1
  stepY=1
  cambio=False

  colors={0:0, 1:0}
  print(realWidthCommands)
  print()
  print(realHeightCommands)

  for sasizza, y in enumerate(realWidthCommands):
    print("valuto", sasizza, y)
    stepY=(stepY+1)%2
    if cambio:
      startColor=(startColor+1)%2
      cambio=False
    if(y[0]==0):
      cambio=True
    color=startColor
    if y[0]!=currentY:
      currentY=y[0]
      continue

    for poppete, x in enumerate(realHeightCommands):
      stepX=(stepX+1)%2
      if(x[0]==stepY):
        color=(color+1)%2

      if(x[0]!=currentX):
        currentX=x[0]
        continue

      if(stepY==1):
        if(y[0]==0):
          if((x[0]==1 and stepX==0)):
            colors[color]=colors[color]+1
            print("da 0 trovato salto dispari PRIMO", color, poppete, "conX1", "lo start color era", startColor)
        else:
          if((x[0]==1 and stepX==1)):
            print("da 1 trovato salto dispari SECONDO", color, poppete, "conX0", "lo start color era", startColor)
            colors[color]=colors[color]+1
      else:
        if(y[0]==0):
          if((x[0]==0 and stepX==0)):
            print("wei da 0 trovato salto dispari PRIMO", color, poppete, "conX0", "lo start color era", startColor)
            colors[color]=colors[color]+1
        else:
          if((x[0]==0 and stepX==1)):
            print("wei da 1 trovato salto dispari SECONDO", color, poppete, "conX1", "lo start color era", startColor)
            colors[color]=colors[color]+1



  print(colors)
  return max(colors.values())

def buildColors(arrayCommands, possibility, currentX):
  yState=possibility[0]
  stepY=possibility[1]
  stepX=0
  color=0
  colors={0:0, 1:0}
  if arrayCommands[0]==stepY:
    color=(color+1)%2
  for num, x in enumerate(arrayCommands):
    stepX=(stepX+1)%2
    if(x==stepY):
      color=(color+1)%2
    if(x!=currentX):
      currentX=x
      continue
    if(yState==0):
      if(stepY==0):
        if((x==0 and stepX==0)):
          colors[color]=colors[color]+1
      else:
        if((x==1 and stepX==0)):
          colors[color]=colors[color]+1
    else:
      if(stepY==0):
        if((x==0 and stepX==1)):
          colors[color]=colors[color]+1
      else:
        if((x==1 and stepX==1)):
          colors[color]=colors[color]+1
  return colors

def buildPreCache(realHeightCommands,currentX, width):
  times=width//(len(realHeightCommands)-1)
  modulo=width%(len(realHeightCommands)-1)
  
  # print("AA", times, modulo, width, len(realHeightCommands), realHeightCommands)

  preCache={}
  possibilities=[(1,0), (1,1), (0,0), (0,1)]
  for possibility in possibilities:
    colors={0:0, 1:0}
    if times!=0:
      colors= buildColors(realHeightCommands, possibility, realHeightCommands[0]+1)
      colors={x:times*y for x,y in colors.items()}
    newColors=buildColors(realHeightCommands[:modulo+1], possibility, realHeightCommands[0]+1)
    colors[0]=colors[0]+newColors[0]
    colors[1]=colors[1]+newColors[1]
    preCache[possibility]=colors
  return preCache

def solve3():
  rows=openFile("raw.txt")
  width, height, widthCommands, heightCommands=parseRows(rows)

  widthCommands=widthCommands*2+widthCommands[0]
  heightCommands=heightCommands*2+heightCommands[0]

  # widthCommands=widthCommands*(height//len(widthCommands)+1)
  # heightCommands=heightCommands*(width//len(heightCommands)+1)

  realWidthCommands=[int(x) for x in widthCommands]
  realHeightCommands=[int(x) for x in heightCommands]

  startColor=int(widthCommands[0])

  currentX=int(heightCommands[0])+1
  currentY=int(widthCommands[0])+1
  stepY=1
  cambio=False

  colors={0:0, 1:0}
  preCache=buildPreCache(realHeightCommands, currentX, width)
  print(preCache)

  for num, y in enumerate(realWidthCommands):
    stepY=(stepY+1)%2
    if cambio:
      startColor=(startColor+1)%2
      cambio=False
    if(y==0):
      cambio=True
    if y!=currentY:
      currentY=y
      continue
    
    colors[0]=colors[0]+preCache[(y, stepY)][(startColor+1)%2]
    colors[1]=colors[1]+preCache[(y, stepY)][startColor]



  times=height//(len(realWidthCommands)-1)
  modulo=height%(len(realWidthCommands)-1)

  # print("hello", times, modulo)
  # print(colors)
  print(colors, times, modulo, len(realWidthCommands)-1)

  colors[0]=colors[0]*times
  colors[1]=colors[1]*times
  stepY=0
  startColor=int(widthCommands[0])
  currentY=int(widthCommands[0])+1

  if times>0:
    currentY=realWidthCommands[-1]

  cambio=False
  for num, y in enumerate(realWidthCommands[:modulo]):
    stepY=(stepY+1)%2
    
    if cambio:
      cambio=False
      startColor=(startColor+1)%2
    if(y==0):
      cambio=True
    if y!=currentY:
      currentY=y
      continue
    
    colors[0]=colors[0]+preCache[(y, stepY)][(startColor+1)%2]
    colors[1]=colors[1]+preCache[(y, stepY)][startColor]


  print(colors)
  return max(colors.values())




# print(solve2())
print(solve3())