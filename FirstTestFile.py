import os 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
objects = [['Jupiter', '-2.7°F', '-234°F', '4.2-6.2 AU', '5.2 AU'], 
           ['Saturn', 'mag', 'temp', 'distearth', 'distsun'],
           ['Venus', 'mag', 'temp', 'distearth', 'distsun'],
           ['Mars', 'mag', 'temp', 'distearth', 'distsun'],
           ['Mercury', 'mag', 'temp', 'distearth', 'distsun'],
           ['Neptune', 'mag', 'temp', 'distearth', 'distsun'],
           ['Uranus', 'mag', 'temp', 'distearth', 'distsun']]
df = pd.DataFrame(objects, columns=["Objects", "Magnitude", 'Surface Temp','Distance from Earth', 'Distance from sun'])
ObjectOfChoice = str(input('What is your chosen object?'))
for i in range (len(objects)):
    i += 1

    print(i)
    Data = pd.Series(objects)
    print(Data)