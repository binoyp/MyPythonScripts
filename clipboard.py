# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 11:03:52 2015

@author: Binoy
"""

import win32clipboard

# set clipboard data
#win32clipboard.OpenClipboard()
#win32clipboard.SetClipboardText('testing 123')
#win32clipboard.CloseClipboard()

# get clipboard data
win32clipboard.OpenClipboard()
data = win32clipboard.GetClipboardData()
print data
win32clipboard.CloseClipboard()
outdat = data.replace('"\n"','","')
print outdat



# set clipboard data
#win32clipboard.OpenClipboard()
#win32clipboard.SetClipboardText('testing 123')
#win32clipboard.CloseClipboard()
