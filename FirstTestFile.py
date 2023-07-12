import os 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
objects = [['Jupiter', 'Magnitude of -2.7', 'Surface temp of -234°F', 'Between 4.2 and 6.2 AU from earth', '5.2 AU from sun'], 
           ['Saturn', 'Magnitude of -0.55', 'Surface temp of -288°F', '7 AU from earth', '9.5 AU from sun'],
           ['Venus', 'Magnitude of -4.6', 'Surface temp of 900°F', 'Around 0.43 AU from earth', '0.72 AU from sun'],
           ['Mars', 'Magnitude of 1.76', 'Surface temp of between 70° and -225°F', '2.23 AU from Earth', '1.5 AU from the sun'],
           ['Mercury', 'mag', 'temp', 'distearth', 'distsun'],
           ['Neptune', 'mag', 'temp', 'distearth', 'distsun'],
           ['Uranus', 'mag', 'temp', 'distearth', 'distsun']]
df = pd.DataFrame(objects, columns=["Objects", "Magnitude", 'Surface Temp','Distance from Earth', 'Distance from sun'])
print(df)
ObjectOfChoice = str(input('What is your chosen object?'))
Search = df.query("Objects == @ObjectOfChoice")
print(Search)