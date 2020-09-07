# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 08:15:59 2020

@author: gunn3
"""
import pandas as pd
import numpy as np
from pybaseball import statcast

df = statcast(start_dt='2017-03-01',end_dt='2020-08-24')

df.to_csv('data\\statcast.csv')
