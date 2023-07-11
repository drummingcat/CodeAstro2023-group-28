import os 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
objects = ['Jupiter', 'Saturn', 'Venus', 'Mars', 'Mercury', 'Neptune', 'Uranus'] #This will be our objects
magnitude = ['mag', 'mag', 'mag', 'mag', 'mag', 'mag', 'mag'] #This will be our magnitudes
surface_temp = ['temp', 'temp', 'temp', 'temp', 'temp', 'temp', 'temp'] #This will be our surface temps
Dist_from_earth = ['Dist', 'Dist', 'Dist', 'Dist', 'Dist','Dist', 'Dist']
Dist_from_sun = ['Dist2', 'Dist2', 'Dist2', 'Dist2', 'Dist2','Dist2', 'Dist2']


s = pd.Series(objects,magnitude,surface_temp,Dist_from_earth,Dist_from_sun) #It will concatenate as long as it is in the dataframe

print(s) 
"""
class skew(object):
  def __init__(self):
    altitude = float(input('What is your latitude'))
    object = str(input('What object would you want to see?'))
  def calc()

Stellarium has a large database of deep sky objects and stars, and it is all open source. This is what I believe could be used in some way for the data for this program: https://stellarium-web.org

"""
