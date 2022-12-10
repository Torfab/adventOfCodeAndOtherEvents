def openFile(path):
  file= open(path, 'r')
  rows= []
  i=0
  while(True):
    row=file.readline().strip()
    if not row: 
      break
    rows.append(row)
    i+=1
  return rows