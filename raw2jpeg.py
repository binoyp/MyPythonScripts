# -*- coding: utf-8 -*-
"""
Created on Fri May 16 23:14:48 2014

@author: Binoy Pilakkat
"""

import os


import xml.etree.ElementTree as ET #Module for xml editing

def genSettingsfiles(inpFold,template,outFold):
    """
    Generates ufraw id files for conversion of raw images to jpeg using ufraw
    specify the input folder containing raw images
    specify a ufraw id template. Using this template new id files are generated
    for conversion using ufraw batch command
    Script executes the ufraw batch command using the newly generated id files.

    """
    _fl = os.listdir(inpFold) #Input folder with raw images
    xm = open(template,'r')    # Sample ufraw id file as template
    data = xm.read()

    xm.close()


    tree = ET.parse(r'K:\Pics\test.ufraw')
    root = tree.getroot()
    for e in _fl:
        if e[-3:] == "CR2":
            inpf = os.path.join(inpFold,e)
            of = e[:-4]+'.jpg'
            ur = e[:-4]+'.ufraw'
            outf= os.path.join(outFold,of) #Output Folder path
            urf = os.path.join(r'K:\Pics\ufraws',ur) #Generated ufraw id files
                                                        #path
            print outf

        for child in root.iter('OutputFilename'):
          child.text = outf
        for child in root.iter('InputFilename'):
          child.text = inpf
          print child.text
        tree.write(urf)
def convert2jpeg(ufrawfold):
    """
    Convert raw files to jpeg in batch using the generated ufraw id files
    """
    cmd = '"C:\\Program Files (x86)\\UFRaw\\bin\\ufraw-batch.exe" --conf= '
    for f in os.listdir(ufrawfold):
        exc = cmd + os.path.join(ufrawfold,f)
        print exc
        run = os.system(exc)
        print run
        if run:
            print "Error in execution\n Aborting.....",
            break
            
        
inpfolder = r'D:\kottiyoor and thirunnelli'
templ =  r'D:\kottiyoor and thirunnelli\template.ufraw'
outfolder = r'K:\Pics\Kottiyoor N Thirunnelli'
#genSettingsfiles(inpfolder,templ,outfolder)
ufo = r'K:\Pics\ufraws'
convert2jpeg(ufo)

