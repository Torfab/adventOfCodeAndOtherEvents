from utility import *

def parseRows(rows):
  width=int(rows[0].split("=")[1])
  height=int(rows[1].split("=")[1])
  widthCommands=rows[2].split("=")[1]
  heightCommands=rows[3].split("=")[1]
  
  return  width, height, widthCommands, heightCommands

def buildColors(arrayCommands, possibility):
  currentX=arrayCommands[0]+1
  yState=possibility[0]
  stepY=possibility[1]
  stepX=0
  color=0
  colors={0:0, 1:0}
  if arrayCommands[0]==stepY:
    color=(color+1)%2
  for x in arrayCommands:
    stepX=(stepX+1)%2
    if(x!=stepY):
      color=(color+1)%2
    if(x!=currentX):
      currentX=x
      continue
    if(yState==0):
      if(stepY==0):
        if((x==1 and stepX==0)):
          colors[color]=colors[color]+1
      else:
        if((x==0 and stepX==0)):
          colors[color]=colors[color]+1
    else:
      if(stepY==0):
        if((x==1 and stepX==1)):
          colors[color]=colors[color]+1
      else:
        if((x==0 and stepX==1)):
          colors[color]=colors[color]+1
  return colors

def buildPreCache(realHeightCommands,currentX, width):
  times=width//(len(realHeightCommands)-1)
  modulo=width%(len(realHeightCommands)-1)
  
  preCache={}
  possibilities=[(1,0), (1,1), (0,0), (0,1)]
  for possibility in possibilities:
    colors={0:0, 1:0}
    if times!=0:
      colors= buildColors(realHeightCommands, possibility)
      colors={x:times*y for x,y in colors.items()}
    newColors=buildColors(realHeightCommands[:modulo+1], possibility)
    colors[0]=colors[0]+newColors[0]
    colors[1]=colors[1]+newColors[1]
    preCache[possibility]=colors
  return preCache

def updateColors(realWidthCommands, preCache):
  
  currentY=int(realWidthCommands[0])+1
  stepY=1
  cambio=False
  startColor=int(realWidthCommands[0])

  colors={0:0, 1:0}
  
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
  return colors

def solve(part):
  rows=openFile("raw.txt")
  width, height, widthCommands, heightCommands=parseRows(rows)

  widthCommands=widthCommands*2+widthCommands[0]
  heightCommands=heightCommands*2+heightCommands[0]

  realWidthCommands=[int(x) for x in widthCommands]
  realHeightCommands=[int(x) for x in heightCommands]

  currentX=int(heightCommands[0])+1
  preCache=buildPreCache(realHeightCommands, currentX, width)

  times=height//(len(realWidthCommands)-1)
  modulo=height%(len(realWidthCommands)-1)
  if(times>0):
    colors=updateColors(realWidthCommands, preCache)
  else:
    colors={0:0, 1:0}

  colors[0]=colors[0]*times
  colors[1]=colors[1]*times


  newColors=updateColors(realWidthCommands[:modulo+1], preCache)
  colors[0]=colors[0]+newColors[0]
  colors[1]=colors[1]+newColors[1]
  if part==1:
    return sum(colors.values())

  return max(colors.values())

# solve(1)
# solve(1)
solve(3)
