# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 08:15:59 2020

@author: gunn3
"""
import pandas as pd
import numpy as np
from pybaseball import statcast

df = statcast(start_dt='2019-03-20',end_dt='2019-04-21')

df.head()

df.game_date.min()

df.to_csv('data\\statcast.csv')
