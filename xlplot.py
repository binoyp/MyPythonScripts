# -*- coding: utf-8 -*-
"""
Created on Thu Aug 06 14:35:53 2015

@author: Binoy
"""

from xlwings import Range, Workbook
import os
from matplotlib import pyplot as plt
import numpy as np
import matplotlib as mpl
mpl.use("pgf")
path = r'C:\Users\Binoy\Documents\Python Scripts'
wb = Workbook(os.path.join(path,"plot.xlsx"))
dat = Range('A2',asarray=1).table.value

styles = ['-', '--', '-.', ':']
markers = list('+ox^psDv')

dat.sort(axis=0)
x = dat[ :, 0]
y = dat[ :, 1]
plt.plot(x, y, marker ='x', linestyle = ':', color ='r')
plt.grid(1)
plt.xlabel(str(Range('A1').value))
plt.ylabel(str(Range('B1').value))
plt.title('Wave Resistance')
plt.show()