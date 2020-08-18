# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 11:48:20 2020

@author: Ben
"""

import pandas as pd
from pybaseball import team_batting
from pybaseball import team_pitching
from pybaseball import standings


def get_nickname(string):
    problems = ['Jays','Sox']
    if string.split(' ')[-1] in problems:
        return ' '.join(string.split(' ')[-2:])
    else:
        return string.split(' ')[-1]

years = [2019,2018,2017,2016,2015]
df_list = []
df2_list = []

for year in years:
    ## get team batting stats and W/L
    df = team_batting(year)
    df2 = team_pitching(year)
    wl = standings(year)

    ## clean up the standings so that it's one df of (name, wins)
    wl = pd.concat(wl).reset_index()
    wl['nickname'] = wl.Tm.apply(lambda x: get_nickname(x))
    wl = wl.loc[:,['nickname','W']]

    ## merge the wins into the stats df, add this df to the list.
    df = df.merge(df2, on=['Season','Team'], suffixes=['_bat','_pitch'])
    df = df.merge(wl,left_on='Team',right_on='nickname')
    df.drop(labels='nickname',axis=1,inplace=True)
    df.rename(columns={''})
    df_list.append(df)
#    df2_list.append(df2)

out_df = pd.concat(df_list)
out_df.to_csv('data//team_stats.csv')

# out_df2 = pd.concat(df2_list)
# out_df2.to_csv('data//team_pitching_stats.csv')