# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 21:32:19 2020

@author: gunn3
"""
import pandas as pd
import numpy as np

pd.options.display.max_rows = 1000

df = pd.read_csv('data\\statcast.csv')
print(df.dtypes)
keep_columns = ['pitch_type',
                'game_date',
                'release_speed',
                'release_pos_x',
                'release_pos_z',
                'player_name',
                'batter',
                'pitcher',
                'zone',
                'game_type',
                'stand',
                'p_throws',
                'home_team',
                'away_team',
                'type',
                'des',
                'game_year',
                'pfx_x',
                'pfx_z',
                'plate_x',
                'plate_z',
                'vx0',
                'vy0',
                'vz0',
                'ax',
                'ay',
                'az',
                'sz_top',
                'sz_bot',
                'launch_speed',
                'launch_angle',
                'launch_speed_angle',
                'estimated_woba_using_speedangle',
                'effective_speed',
                'release_spin_rate',
                'release_extension',
                'woba_value',
                'woba_denom']

df = df.loc[:,keep_columns]
p_woba_against = pd.pivot_table(df,
                                index=['player_name','game_year'],
                                values=['woba_value','woba_denom'],
                                aggfunc=np.sum)

p_woba_against['woba_against'] = p_woba_against.woba_value / p_woba_against.woba_denom

df.to_csv('data\\statcast_cleaned.csv')
