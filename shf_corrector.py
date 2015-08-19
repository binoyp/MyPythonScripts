# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 09:47:27 2015

@author: Binoy
"""
import re, math
from matplotlib import pyplot as plt

def main():
    pattern1 = re.compile('^[a-zA-Z]+$')
    
    f = open(r"D:\Internship-Shipflow\Hull2\off_hull2split.shf")
    outf = open(r"D:\Internship-Shipflow\Hull2\off_hull2split-p.shf",'w')
    lineno =1
    stnflag = 0
    for line in f:
        match = re.search(pattern1, line.strip())
        if match:
            #print line.replace(match.group(),'____')
            print lineno, line
            outf.write(line)

            
        else:
            coords = line.split()
            cur_x = coords[0]
            cur_y = coords[1]
            cur_z = coords[3]
            ws1 =  18* ' '
            ws2 = 10 * ' '
            ws3 =  10 * ' '
            ws4 = 18 * ' '
            outf.write(ws1 + coords[0] + ws2 + str(abs(float(coords[1]))) + ws3 + str(abs(float(coords[2]))) + ws4 + coords[-1]+'\n' )
            

        lineno += 1
  
#        if line.strip() == 'end':
#            print lineno
#    
    outf.close()


if __name__ == "__main__":
    main()