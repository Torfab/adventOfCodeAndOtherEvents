from utility import *


rows=openFile("input.txt")

rows=[int(a) for a in rows]
lines=len(rows)

start=0
end=60
count=0
while(end<lines):
  accumulatore=0
  for a in range(start, end):
    accumulatore=accumulatore+rows[a]
  accumulatore=accumulatore/60
  if(accumulatore<1500 or accumulatore>1600):
    count=count+1
  start=start+1
  end=end+1
print(count)