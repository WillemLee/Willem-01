#/umesr/bin/env python3
import json,sys
import pandas as pd
import matplotlib.pyplot as plt
from pandas import Series,DataFrame
import numpy as np

class StudentLearn():
    def analysis(self):
        self.minutes_dict = self.StudentData.groupby('user_id').sum()
    def __init__(self):
         try:
            self.StudentData = pd.read_json('user_study.json')
         except ValueError:
            return None
    def draw(self):
          fig = plt.figure()
          ax = fig.add_subplot(1,1,1)
          ax.set_title("StudyData")
          id_major_ticks = np.arange(0,224000,4000)
          id_minor_ticks = np.arange(0,224000,500)
          minu_major_ticks = np.arange(0,500,50)
          minu_minor_ticks = np.arange(0,500,5)
          ax.set_xticks(id_major_ticks)
          ax.set_xticks(id_minor_ticks,minor=True)
          ax.set_yticks(minu_major_ticks)
          ax.set_yticks(minu_minor_ticks,minor=True)
          ax.set_ylabel('Study Time')
          ax.set_xlabel('User ID')
          self.minutes_dict.plot()
          plt.show()

if __name__ == '__main__':
    a = StudentLearn()
    a.analysis()
    a.draw()
    
