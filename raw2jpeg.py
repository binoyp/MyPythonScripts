# -*- coding: utf-8 -*-
"""
Created on Fri May 16 23:14:48 2014

@author: Binoy Pilakkat
"""

import os


import xml.etree.ElementTree as ET
def genSettingsfiles():
    _fl = os.listdir(r'F:\DCIM\100CANON')
    xm = open(r'K:\Pics\test.ufraw','r')
    data = xm.read()
    
    xm.close()
    
    
    tree = ET.parse(r'K:\Pics\test.ufraw')
    root = tree.getroot()
    for e in _fl:
        if e[-3:] == "CR2":
            inpf = os.path.join(r'F:\DCIM\100CANON',e)
            of = e[:-4]+'.jpg'
            ur = e[:-4]+'.ufraw'
            outf= os.path.join(r'K:\Pics',of)
            urf = os.path.join(r'K:\Pics\ufraws',ur)
            print outf
cmd = '"C:\\Program Files (x86)\\UFRaw\\bin\\ufraw-batch.exe" --conf= '
for f in os.listdir(r'K:\Pics\ufraws'):
    exc = cmd + os.path.join(r'K:\\Pics\\ufraws',f)
    print exc  
    run = os.system(exc)    
    print run
    if run:
        break            
#        for child in root.iter('OutputFilename'):
#          child.text = outf
#        for child in root.iter('InputFilename'):
#          child.text = inpf
#          print child.text
#        tree.write(ur)
