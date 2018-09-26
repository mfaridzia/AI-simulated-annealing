import random
import math

# simulated function
def simulatedFunc(x1, x2):
  try:
    value = -1 * abs(math.sin(x1) * math.cos(x2) * math.exp(abs(1 - (math.sqrt((x1 ** 2) + (x2 ** 2)) / math.pi))))
  except OverflowError:
    value = float('inf')
  return value

def changes(delt, temp):
  return math.exp(-delt / temp)

# random function
def randNum(val):
  newVal = val + random.uniform(-10, 10)
  while (newVal > 10) or (newVal < -10):
    newVal = val + random.uniform(-10, 10)
  return newVal

currentValue1 = random.uniform(-10, 10)
currentValue2 = random.uniform(-10, 10)
bestValue = simulatedFunc(currentValue1, currentValue2)

cooling = 0.8
T = 10000 #temperature
N = 1 #init value

while T > N:
  newVal1 = randNum(currentValue1)
  newVal2 = randNum(currentValue2)
  currentFunc = simulatedFunc(currentValue1, currentValue2)
  newFunc = simulatedFunc(newVal1, newVal2)
  delta = newFunc - currentFunc

  #check if new value < current value
  if (newFunc < currentFunc):
      currentValue1 = newVal1
      currentValue2 = newVal2
      bestValue = simulatedFunc(newVal1, newVal2)
  else:
      randomNumber = random.uniform(0, 1) #generate random number
      dec = changes(delta, T)
      if (randomNumber < dec):
          currentValue1 = newVal1
          currentValue2 = newVal2
  print("Minimum value: %f" %bestValue) #temporary result
  T *= cooling
print("Result for minimum value: %f" %bestValue) #final result
