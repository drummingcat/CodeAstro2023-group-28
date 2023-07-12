import os 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
objects = [['Object: Jupiter', 'Magnitude of -2.7', 'Surface temp of -234°F', 'Between 4.2 and 6.2 AU from earth', '5.2 AU from sun'], 
           ['Object: Saturn', 'Magnitude of -0.55', 'Surface temp of -288°F', '7 AU from earth', '9.5 AU from sun'],
           ['Object: Venus', 'Magnitude of -4.6', 'Surface temp of 900°F', 'Around 0.43 AU from earth', '0.72 AU from sun'],
           ['Object: Mars', 'Magnitude of 1.76', 'Surface temp of between 70° and -225°F', '2.23 AU from Earth', '1.5 AU from the sun'],
           ['Object: Mercury', 'mag', 'temp', 'distearth', 'distsun'],
           ['Object: Neptune', 'mag', 'temp', 'distearth', 'distsun'],
           ['Object: Uranus', 'mag', 'temp', 'distearth', 'distsun']]
length = (len(objects))
df = pd.DataFrame(objects, columns=["Objects", "Magnitude", 'Surface Temp','Distance from Earth', 'Distance from sun'])
ObjectOfChoice = str(input('What is your chosen object?'))
for i in range (length):
    i += 1
    print(i)
if ObjectOfChoice == 'Jupiter':
    i = 0
    Data = pd.Series(objects[i])
    print(Data)
if ObjectOfChoice == 'Saturn':
    i = 1
    Data = pd.Series(objects[i])
    print(Data)