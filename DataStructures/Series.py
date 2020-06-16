# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 13:12:06 2020

@author: buyewen
"""

import pandas as pd
import numpy as np

#create a series
#s = pd.Series(data, index = index)

#from ndarray
s = pd.Series(np.random.randn(5), index = ["a", "b", "c", "d", "e"])
print(s)
print(s.index)
s = pd.Series(np.random.randn(5))
print(s)

#from dict
d = {"b": 1, "a": 0, "c": 2}
s = pd.Series(d)
print(s)
s = pd.Series(d, index = ["a", "b", "c", "d", "e"])
print(s)

#from scalar value
s = pd.Series(5., index = ["a", "b", "d", "d"])
print(s)

#operate as NumPy function
s = pd.Series(np.random.randn(5), index = ["a", "b", "c", "d", "e"])
print(s)    #原数组
print(s[0]) #第0个数
print(s[:3])    #前3个数
print(s[s > s.median()])    #大于中位数的数
print(s[[4, 3, 1]]) #第4，3，1个数
print(np.exp(s))    #e的幂次方，e=2.71828
print(s.dtype)  #数组类型
print(s.array)  #扩展的数组数据
print(s.to_numpy())   #真实的numpy数组数据

#operate as Dict function
print(s["a"])
s["e"] = 12.
print(s)
print("e" in s)
print("f" in s)
print(s.get("f"))
print(s.get("f", np.nan))
print(s)
s["f"] = 10.
print(s)

#vectorized operation
print(s + s)
print(s * 2)
print(np.exp(s))
print(s[1:] + s[:-1])

#can have name
s = pd.Series(np.random.randn(5), name = "something")
print(s)
print(s.name)
s2 = s.rename("different")
print(s2)
print(s2.name)