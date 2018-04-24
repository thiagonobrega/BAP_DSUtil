# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 13:28:58 2018

@author: Thiago
"""
import pandas as pd
import numpy as np
from parsers import base
import os
from datetime import datetime

def readFile(in_dir,file):
    return base.readData(in_dir+file, sep=",")

outdir ="F:"+os.path.sep+"z_dados"+os.path.sep+"drugs"+os.path.sep
indir=outdir+"fda"+os.path.sep
base.writeData(data,outdir+)
data_demo = readFile(outdir,'drugs_fda.csv')