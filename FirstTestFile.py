import os 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
objects = [['Jupiter', 'mag', 'temp', 'distearth', 'distsun'], 
           ['Saturn', 'mag', 'temp', 'distearth', 'distsun'],
           ['Venus', 'mag', 'temp', 'distearth', 'distsun'],
           ['Mars', 'mag', 'temp', 'distearth', 'distsun'],
           ['Mercury', 'mag', 'temp', 'distearth', 'distsun'],
           ['Neptune', 'mag', 'temp', 'distearth', 'distsun'],
           ['Uranus', 'mag', 'temp', 'distearth', 'distsun']]
df = pd.DataFrame(objects, columns=["Objects", "Magnitude", 'Surface Temp','Distance from Earth', 'Distance from sun'])
df