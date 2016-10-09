# -*- coding: utf-8 -*-
import os
import wx

keyW = raw_input('searching for:\n')
dirname = raw_input('path:\n')
for roots, dirs, files in os.walk(dirname):
    for file in files:
        if keyW in file:
            print (roots + '\\' + file)
        print (roots + '\\' + file)
        onefile = open(roots + '\\' + file, 'r')
        content = onefile.read()
        if keyW in content:
            print (roots + '\\' + file)
