
raw=rew.split("\n")

def parseRow(raw):
    result=[]
    for row in raw:
        rowSplitted=row.split(" ")
        configuration=rowSplitted[0][1:-1]
        configurationList=[]
        for element in configuration:
            if element==".":
                configurationList.append(0)
            else:
                configurationList.append(1)
        finalObject={}
        finalObject["configuration"]=tuple(configurationList)
        buttons=[]
        for button in rowSplitted[1:-1]:
            buttons.append([int(x) for x in button[1:-1].split(",")])
        finalObject["buttons"]=buttons
        result.append(finalObject)
    return result

def findCombination(configuration, buttons):
    state=[0]*len(configuration)
    buttonsPressed=[-1]
    newStates=[]
    newStates.append((state, buttonsPressed))
    states=[]
    iteration=0
    while(newStates):
        states=newStates
        newStates=[]
        iteration=iteration+1
        while(states):
            state, buttonPressed=states.pop()
            lastButtonPressed=buttonPressed[-1]
            for i in range(lastButtonPressed+1, len(buttons)):
                tentativeState=state.copy()
                for el in buttons[i]:
                    tentativeState[el]=(tentativeState[el]+1)%2
                if tuple(tentativeState)==configuration:
                    return i, buttonPressed[1:]+[el]
                else:
                    newStates.append((tentativeState, buttonPressed+[i]))
        #print(newStates)
    print("oh no")
    return
def solve():
    schematics=parseRow(raw)
    count=0
    for schematic in schematics:
        configuration=schematic["configuration"]
        buttonList=schematic["buttons"]
        turnedOn=[]
        for i, element in enumerate(configuration):
            if element==1:
                turnedOn.append(i)
        filteredButtons=[]
        for button in buttonList:
            if any(item in turnedOn for item in button):
                filteredButtons.append(button)
            
        iteration, pressedButtons=findCombination(configuration, filteredButtons)
        print(iteration, pressedButtons)
        count=count+iteration 
            
    return count

print(solve())
