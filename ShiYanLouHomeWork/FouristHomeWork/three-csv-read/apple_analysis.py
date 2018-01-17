#/usr/env/bin python3
# -*- coding:utf-8 -*-
import pandas as pd
def quarter_volume():
    data = pd.read_csv('apple.csv',header=0)
    
    Year_succ = data.Volume

    Year_succ.index = pd.to_datetime(data.Date)

    second_volume = Year_succ.resample("Q").sum().sort_values()[-2]

    return second_volume
