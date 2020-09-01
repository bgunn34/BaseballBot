# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 12:34:58 2020

@author: Ben
"""

import pandas as pd
import numpy as np
from pybaseball import batting_stats
from pybaseball import pitching_stats

df = batting_stats(2017,2019,qual=50)
df.to_csv('data\\batters_hist.csv')
df = batting_stats(2020,qual=50)
df.to_csv('data\\batters_year.csv')
df = pitching_stats(2017,2019,qual=50)
df.to_csv('data\\pitchers_hist.csv')
df = pitching_stats(2020)
df.to_csv('data\\pitchers_year.csv')
