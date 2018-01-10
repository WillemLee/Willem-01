#/umesr/bin/env python3
import json,sys
import pandas as pd

def analysis(filename,user_id):
    times = 0
    minutes = 0
    try:
       us = pd.read_json(filename)
    except ValueError:
       return 0,0


    times = us[us['user_id']==int(user_id)].minutes.count()
    minutes = us[us['user_id']==int(user_id)].minutes.sum()
    print(times,minutes)
    return times,minutes


if __name__ == '__main__':
    analysis(sys.argv[1],sys.argv[2])
