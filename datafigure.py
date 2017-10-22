# -*- coding: utf-8 -*-

import json
import pandas as pd
import os
import matplotlib.pyplot as plt

def analysis(file, user_id):
    times = 0
    minutes = 0
    
    file_exists = os.path.exists(file)
    if file_exists is True:
        df = pd.read_json(file, typ='frame')
        times = df[df['user_id'] == user_id]['minutes'].size
        minutes = df[df['user_id'] == user_id]['minutes'].sum()

    return times, minutes


if __name__ == '__main__':
    filename = '/home/shiyanlou/Code/user_study.json'
    df = pd.read_json(filename, typ='frame')
    resdf = df[['user_id','minutes']].groupby('user_id').sum()
    lessdf = resdf.iloc[0:100]

    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)

    ax.set_title('StudayData')

    ax.set_xlabel('User ID')
    ax.set_ylabel('Study Time')
    
    x = lessdf.index
    y = lessdf.minutes
    
    ax.plot(x,y)
    fig.show()
    input()
