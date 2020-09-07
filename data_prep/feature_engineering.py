# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 17:35:43 2020

@author: Ben
"""

import pandas as pd
import numpy as np
#from collections import counter

df = pd.read_csv('data\\retro_cleaned.csv')
df['visit_win'] = df.apply(lambda x: 1 if x.visiting_score > x.home_score else 0,axis=1)
df['home_win'] = df.apply(lambda x: 1 if x.visiting_score < x.home_score else 0,axis=1)
df.dtypes.tail(20)

v_lineup = [
    'visiting_1_name',
    'visiting_2_name',
    'visiting_3_name',
    'visiting_4_name',
    'visiting_5_name',
    'visiting_6_name',
    'visiting_7_name',
    'visiting_8_name',
    'visiting_9_name']
h_lineup = [
    'home_1_name',
    'home_2_name',
    'home_3_name',
    'home_4_name',
    'home_5_name',
    'home_6_name',
    'home_7_name',
    'home_8_name',
    'home_9_name']

## get a list of players
batters = []
for col in v_lineup:
    batters = batters + df[col].tolist()
for col in h_lineup:
    batters = batters + df[col].tolist()
## remove duplicates
batters = list(set(batters))

## split the df along winning team and segregate the lineups.
h_win_line = df.loc[df.home_win == 1,h_lineup]
v_win_line = df.loc[df.home_win == 1,v_lineup]
## iterate through that list, check if that player exists on the winning side.
wins_list = []
for col in h_win_line.columns:
    wins_list.append(h_win_line[col].value_counts().reset_index())
for col in v_win_line.columns:
    wins_list.append(v_win_line[col].value_counts().reset_index())
    
wins = pd.concat(wins_list)
wins = wins.fillna(0)
wins.loc[:,'wins'] = wins.sum(axis=1)
wins.rename(columns={'index':'name'},inplace=True)
wins = wins.loc[:,['name','wins']]
## pivot table
wins = pd.pivot_table(wins,index='name',values='wins',aggfunc=np.sum).reset_index()

## I got a list of players and the wins they contributed to. Now that I have it, I am not sure how useful it actually is.

