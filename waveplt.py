# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 15:55:39 2015

@author: admin
"""

import matplotlib.pyplot as plt
import numpy as np

_LPP = 36.02

def LWCUT_parser(path):
    f = open(path,'r')
    dictWave = {}
    loc = f.readline()
    while loc:
        count = int(f.readline())
        dat = np.zeros((count,2))
        for i in range(count):
            dat[i,:]=[float(v)*_LPP for v in f.readline().split()]
        np.sort(dat,axis=-1)
        dictWave[float(loc)] = dat
        dat2 = dat[ (38>dat[:,0]) & (dat[:,0]>-2) ]
        loc = f.readline()
    f.close()
    return dictWave

def pltDic(_dic, lpp, opt = 'all'):
    npt = len(_dic)
    locs = _dic.keys()

    if opt == 'all':
        fig, ax = plt.subplots(nrows =npt)
        for i in range(npt):
            ax[i].plot(_dic[locs[i]][:,0], _dic[locs[i]][:,1])
            ax[i].grid(1)
            ax[i].set_title('y loc='+str(locs[i]*lpp))
            ax[i].axvline(lpp)
            ax[i].axvline(0)
    else:
        plt.plot(_dic[opt][:,0], _dic[opt][:,1])
        plt.grid(1)
        plt.title(r'$y/L_{PP}$='+str(opt*lpp))
        plt.xlabel('$x$')
        plt.ylabel('wave height')

#        plt.axvline(lpp)
#        plt.axvline(0)
    plt.tight_layout()
    plt.show()



if __name__ == "__main__":
    path = r"F:\FinalXpanRun\R2velocity=10knots\config2-vel-10kn_RUN_DIR\config2-vel-10kn_LWAVECUT"
    dicW = LWCUT_parser(path)
    print dicW.keys()
    pltDic(dicW, _LPP, -0.001)
