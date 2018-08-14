# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 19:52:08 2018

@author: elikr
"""

def featureScaling(arr):
#rescaling 3 values in a list. 
    values = []
    x_min = 0
    x_max = 0
    x = 0
    count = 0

    for value in arr:
        if value in values:
            count +=1
        else:
            values.append(value)
            values.sort()
    if count == 0:
#check if there are values that are the same.The epxected result is that all \
#values are different.
        x_min = values[0]
        x = values[1]
        x_max = values[2]
    else:
        pass
    fs = (float(x - x_min)/(x_max - x_min))
    
    return fs


# tests of your feature scaler--line below is input data
data = [115, 140, 175]
print featureScaling(data)