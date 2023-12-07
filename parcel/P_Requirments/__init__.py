import sys
import os
from zipfile import ZipFile

class colors:
  red = '\033[91m'
  green = '\033[92m'
  yellow = '\033[93m'
  blue = '\033[94m'
  magenta = '\033[95m'
  cyan = '\033[96m'
  white = '\033[97m'
  end = '\033[0m'



def modesliteralZIPPED(filepassname):
  with ZipFile(filepassname,'w') as zip:
    zip.printdir()
    zip.extractall()

mode = {"zipped":modesliteralZIPPED}

type = {"str":str(),"int":int(),"bool":bool(),"float":float(),"other":None}