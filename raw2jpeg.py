# -*- coding: utf-8 -*-
"""
Created on Fri May 16 23:14:48 2014

@author: Binoy Pilakkat
"""

import os


import xml.etree.ElementTree as ET #Module for xml editing

def genSettingsfiles():
    """
    Generates ufraw id files for conversion of raw images to jpeg using ufraw
    specify the input folder containing raw images
    specify a ufraw id template. Using this template new id files are generated
    for conversion using ufraw batch command
    Script executes the ufraw batch command using the newly generated id files.

    """
    _fl = os.listdir(r'F:\DCIM\100CANON') #Input folder with raw images
    xm = open(r'K:\Pics\test.ufraw','r')    # Sample ufraw id file as template
    data = xm.read()

    xm.close()


    tree = ET.parse(r'K:\Pics\test.ufraw')
    root = tree.getroot()
    for e in _fl:
        if e[-3:] == "CR2":
            inpf = os.path.join(r'F:\DCIM\100CANON',e)
            of = e[:-4]+'.jpg'
            ur = e[:-4]+'.ufraw'
            outf= os.path.join(r'K:\Pics',of) #Output Folder path
            urf = os.path.join(r'K:\Pics\ufraws',ur) #Generated ufraw id files
                                                        #path
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
