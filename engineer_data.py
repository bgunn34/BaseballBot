# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 17:44:18 2020

@author: Ben
"""

import pandas as pd
import numpy as np
from functools import reduce
pd.options.display.max_rows = 500

### input a list of names and output a list of each batter's principal stats
# def get_batters(bats):
#     for bat in bats:
    
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
           'wKN',
           'ERA']

## to do: pivot statcast so that I get a frame of pitchers, years, ff data, then
## another of pitcher year sl data, then merge on pitcher year at the end.

sc = pd.read_csv('data\\statcast.csv')
fg = pd.read_csv('data\\pitchers_hist.csv')

# build a list of dataframes where each is a filtered, pivoted frame of the 
# given pitch selection.

ffs = sc.loc[sc.pitch_type.isin(['FF','FT','SI'])].copy()
sls = sc.loc[sc.pitch_type == 'SL'].copy()
cts = sc.loc[sc.pitch_type == 'FC'].copy()
cbs = sc.loc[sc.pitch_type.isin(['CU','KC','EP'])].copy()
chs = sc.loc[sc.pitch_type == 'CH'].copy()
sfs = sc.loc[sc.pitch_type.isin(['FS','FO'])].copy()
kns = sc.loc[sc.pitch_type == 'KN'].copy()

ff_table = pd.pivot_table(ffs,index=['player_name','game_year'],values=['release_spin_rate','release_extension']).reset_index()
ff_table.columns = ['player_name','year','fb_extension','fb_spinrate']
sl_table = pd.pivot_table(sls,index=['player_name','game_year'],values=['release_spin_rate','release_extension']).reset_index()
sl_table.columns = ['player_name','year','sl_extension','sl_spinrate']
cts_table = pd.pivot_table(cts,index=['player_name','game_year'],values=['release_spin_rate','release_extension']).reset_index()
cts_table.columns = ['player_name','year','ct_extension','ct_spinrate']
cbs_table = pd.pivot_table(cbs,index=['player_name','game_year'],values=['release_spin_rate','release_extension']).reset_index()
cbs_table.columns = ['player_name','year','cb_extension','cb_spinrate']
chs_table = pd.pivot_table(chs,index=['player_name','game_year'],values=['release_spin_rate','release_extension']).reset_index()
chs_table.columns = ['player_name','year','ch_extension','ch_spinrate']
sfs_table = pd.pivot_table(sfs,index=['player_name','game_year'],values=['release_spin_rate','release_extension']).reset_index()
sfs_table.columns = ['player_name','year','sfs_extension','sfs_spinrate']
kns_table = pd.pivot_table(kns,index=['player_name','game_year'],values=['release_spin_rate','release_extension']).reset_index()
kns_table.columns = ['player_name','year','kn_extension','kn_spinrate']


dfs = [ff_table,sl_table,cts_table,cbs_table,chs_table,sfs_table,kns_table]

sc_final = reduce(lambda left,right: pd.merge(left,right,how='left',on=['player_name','year']),dfs)

fg_filtered = fg.loc[:,['Name',
                        'Season',
                        'wFB',
                        'wSL',
                        'wCT',
                        'wCB',
                        'wCH',
                        'wSF',
                        'wKN',
                        'ERA']]

fg_filtered.columns = ['player_name',
                       'year',
                       'wFB',
                       'wSL',
                       'wCT',
                       'wCB',
                       'wCH',
                       'wSF',
                       'wKN',
                       'ERA']

df_final = pd.merge(sc_final,fg_filtered,how='right',on=['player_name','year'])
df_final.to_csv('data\\pitcher_multivar.csv')
