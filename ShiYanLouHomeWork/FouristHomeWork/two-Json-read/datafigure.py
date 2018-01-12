#/umesr/bin/env python3
import json,sys
import pandas as pd
import matplotlib.pyplot as plt
from pandas import Series,DataFrame

class StudentLearn():
    def analysis(self,user_id):
        times = 0
        minutes = 0
        except ValueError:
            return 0,0


         times = us[us['user_id']==int(user_id)].minutes.count()
         minutes = us[us['user_id']==int(user_id)].minutes.sum()
         return times,minutes
    
    def __init__(self):
         try:
            self.StudentData = pd.read_json(user_study.json)
         except ValueError:
             return None

    def piant(self):
          fig = plt.figure()
          ax = fig.add_subplot(1,1,1)

          ax.set_title("Study")

          major_ticks = np.arange()
          minor_ticks = np.arange()

          ax.set_xticks()
          ax.set_xticks()
          ax.set_yticks()
          ax.set_yticks()

          ax.set_xlabel()
          ax.set_ylabel()
