from utilityz import * 
## Oggi mi sono arreso a Z3, quantomeno ho un explainer di come ha fatto
## Da reimplementare come ricerca bisezionale vedi reddit

from z3 import *

def findJoltage(joltage, buttons):
    """
    joltage:  list of integers representing the target state
    buttons:  list of tuples, each tuple is a set of indices incremented by that button
    """

    # ---------------------------------------------------------------------
    # PART 1 — PREPARATION
    # ---------------------------------------------------------------------

    # Number of buttons (one variable per button, the number of times we press it)
    n_buttons = len(buttons)

    # Number of positions in the joltage vector
    n_j = len(joltage)

    # ---------------------------------------------------------------------
    # PART 2 — CREATE Z3 VARIABLES
    # ---------------------------------------------------------------------
    # We need: x_0, x_1, ..., x_(n_buttons-1)
    # Each x_k is the number of times we press button k.
    #
    # These MUST be integers (Z3 Ints), not bitvectors or reals.
    # Bitvectors would introduce unwanted wraparound; reals would allow fractional presses.
    # Int gives us unbounded mathematical integers.
    #
    # They are the unknowns that Z3 will solve for.
    x = [Int(f"x_{k}") for k in range(n_buttons)]

    # We use Optimize() instead of Solver() because we want
    # a MINIMAL solution (fewest total button presses).
    opt = Optimize()

    # ---------------------------------------------------------------------
    # PART 3 — BASIC DOMAIN CONSTRAINTS
    # ---------------------------------------------------------------------
    # Button presses cannot be negative.
    # This is an important constraint because without it, Z3 might solve
    # the equation with negative presses + positive presses canceling out.
    #
    # We do NOT say "x_k is integer" — declaring Int(...) already enforces that.
    for var in x:
        opt.add(var >= 0)

    # ---------------------------------------------------------------------
    # PART 4 — EXPRESS THE REAL MEANING OF A BUTTON PRESS
    # ---------------------------------------------------------------------
    # This is the core of the mathematical model.
    #
    # For each joltage index i (i.e., each position in the final vector),
    # we want:
    #
    #   sum over all buttons k of (x_k * effect of button k on index i) == joltage[i]
    #
    # But buttons are defined as tuples of indices they increment by +1.
    #
    # So effect(button k, index i) = 1 if i is in buttons[k], else 0.
    #
    # Example: if buttons[0] = (0, 2)
    #   index i = 0 → effect = 1
    #   index i = 1 → effect = 0
    #   index i = 2 → effect = 1
    #   index i = 3 → effect = 0
    #
    # Z3 does NOT allow you to multiply booleans directly, so we use If(...,1,0).
    #
    # For each joltage index i:
    #   Σ_k If(i in buttons[k], x_k, 0) == joltage[i]
    #
    for i in range(n_j):

        # Build the sum of contributions from every button k to position i
        contributions = [
            If(i in buttons[k], x[k], 0)   # if button k affects index i → add x[k], otherwise add 0
            for k in range(n_buttons)
        ]

        # Add constraint: sum of contributions must equal joltage[i]
        opt.add(Sum(contributions) == joltage[i])

    # ---------------------------------------------------------------------
    # PART 5 — OBJECTIVE FUNCTION
    # ---------------------------------------------------------------------
    # We want the FEWEST button presses.
    #
    # total_presses = x_0 + x_1 + ... + x_(n_buttons-1)
    #
    # Optimize() will try to minimize this value.
    total_presses = Sum(x)
    opt.minimize(total_presses)

    # ---------------------------------------------------------------------
    # PART 6 — LET Z3 SOLVE
    # ---------------------------------------------------------------------
    if opt.check() == sat:
        model = opt.model()

        return model.evaluate(total_presses).as_long()

    # No solution exists (rare, but useful for validation).
    return None, None



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
    joltage=tuple([int(x) for x in rowSplitted[-1][1:-1].split(",")])
    finalObject["joltage"]=joltage
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
          return iteration, buttonPressed[1:]+[i]
        else:
          newStates.append((tentativeState, buttonPressed+[i]))
    #print(newStates)
  print("oh no")
  return

def solve():
  rows=getOldAocInput(10)
  schematics=parseRow(rows)
  count=0
  for schematic in schematics:
    configuration=schematic["configuration"]
    buttonList=schematic["buttons"]
    turnedOn=[]
    for i, element in enumerate(configuration):
      if element==1:
        turnedOn.append(i)
    iteration, _=findCombination(configuration, buttonList)
    count=count+iteration 
  return count

def solve2():
  rows=getOldAocInput(10)
  schematics=parseRow(rows)
  count=0
  for i, schematic in enumerate(schematics):
    joltage=schematic["joltage"]
    buttonList=schematic["buttons"]
    num=findJoltage(joltage, buttonList)
    count=count+findJoltage(joltage, buttonList)
  return count

print(solve2())
