import * from utility

raw=getOldAocInput(7)

def myMul(a,b):
    return a*b
    
def mySum(a,b):
    return a+b

decodeOperation={"*":myMul, "+":mySum}

def parseRows(raw):
    commandRows=[]
    for row in raw:
        singleRow=[]
        for val in row.split(" "):
            if val!="" and val!=" ":
                singleRow.append(val)
        commandRows.append(singleRow)
    commands=[]
    for i in range(len(commandRows[0])):
        commandColumn=[]
        for element in commandRows:
            commandColumn.append(element[i])
        commands.append(commandColumn)
    return commands
    
def solve():
    commands=parseRows(raw)
    result=0
    for element in commands:
        f=decodeOperation[element[-1]]
        partialRes=int(element[0])
        for i in range(len(element)-2):
            partialRes=f(partialRes, int(element[i+1]))
        result=result+partialRes
    return result
    
def solve2():
    calc="+"
    result=0
    for i in range(len(raw[0])):
        if raw[-1][i] in ["*", "+"]:
            calc=raw[-1][i]
            numbers=[]
        numb=""
        for row in raw[:-1]:
            numb=numb+row[i]
        numb=numb.strip()
        if numb:
            numbers.append(int(numb))
        else:
            partialRes=numbers[0]
            f=decodeOperation[calc]
            for idx in range(len(numbers)-1):
                partialRes=f(partialRes, numbers[idx+1])
            result=result+partialRes
    partialRes=numbers[0]
    f=decodeOperation[calc]
    for idx in range(len(numbers)-1):
        partialRes=f(partialRes, numbers[idx+1])
    result=result+partialRes
    return result    
            

print(solve2())
