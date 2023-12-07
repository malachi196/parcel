'''Welcome to parcel.py! this project was made to "package programs properly".
The contents of this file are original. Creation credits go to @malachi196 on github'''

'''for any items with kwargs, input a variable name, and its value'''

import sys
import os
from zipfile import ZipFile
import P_Requirments as pr #personal module for unnamed functions

class colors:
  red = '\033[91m'
  green = '\033[92m'
  yellow = '\033[93m'
  blue = '\033[94m'
  magenta = '\033[95m'
  cyan = '\033[96m'
  white = '\033[97m'
  end = '\033[0m'
#=====literals=====
ZIPPED = pr.mode['zipped']
STR = pr.type['str']
INT = pr.type['int']
BOOL = pr.type['bool']
FLOAT = pr.type["float"]
MULTI = pr.type['other']

#=====functions=====
def measure(filename): # measures length of contents
  with open(filename,'r') as f: 
    fileno = f.fileno()
    print(fileno)
  
def wrap(type,spacing,**kwargs): # wraps items
  results = ""
  try:
    if type == STR: #str
      if spacing == True:
        for arg in kwargs.values():
          results += arg + " "
          return results
      else:
        for arg in kwargs.values():
          results += arg 
      return results
    elif type == INT: # int
      if spacing == True:
        for arg in kwargs.values():
          results += str(arg) + " "
        return results
      else:
        for arg in kwargs.values():
          results += arg 
    elif type == BOOL: # bool
      if spacing == True:
        for arg in kwargs.values():
          results += str(arg).lower() + " "
        return results.lower()
      else:
        for arg in kwargs.values():
          results += str(arg).lower()
        return results.lower()
    elif type == FLOAT: # float
      if spacing == True:
        for arg in kwargs.values():
          results += str(arg) + " "
        return results
      else:
        for arg in kwargs.values():
          results += str(arg)
    elif type == MULTI: # other
      if spacing == True:
        for arg in kwargs.values():
          results += str(arg).lower() + " "
        return results
      else:
        for arg in kwargs.values():
          results += str(arg).lower()
        return results
  except Exception as e:
    print(f"An error occoured with kwargs. Exception: {e}")
