# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 17:44:18 2020

@author: Ben
"""

### input a list of names and output a list of each batter's principal stats
def get_batters(bats):
    for bat in bats:
    
### I want to read the statcast and output a list of pitcher's average spinrates
### per pitch type per pitcher per year so:
    
columns = ['pitcher name',
           'year',
           'fb_spinrate',
           'fb_extension',
           'sl_spinrate',
           'sl_extension',
           'ct_spinrate',
           'ct_extension',
           'cb_spinrate',
           'cb_extension',
           'ch_spinrate',
           'ch_extension',
           'sf_spinrate',
           'sf_extension',
           'kn_spinrate',
           'kn_extension',
           'wFB',
           'wSL',
           'wCT',
           'wCB',
           'wCH',
           'wSF',
           'wKN']

## to do: pivot statcast so that I get a frame of pitchers, years, ff data, then
## another of pitcher year sl data, then merge on pitcher year at the end.