# -*- coding: utf-8 -*-
"""
Created on Fri May 21 13:33:55 2021

@author: Devineni
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
pd.options.plotting.backend = "matplotlib"
# functions to print in colour
def prRed(skk): print("\033[31;1;m {}\033[00m" .format(skk)) 
def prYellow(skk): print("\033[33;1;m {}\033[00m" .format(skk)) 
import os
# =============================================================================
# sensor_list = ['1c', '3b', '2L', '2e', 'außen', '1T', '2a_50', '2c_50', '2d', '4T', '3h', 
#      '3L_Kü', '2T', '4L', '3d', '1L', '3a_50']
# pos = pd.read_excel("C:/Users/Devineni/OneDrive - bwedu/6_Recirculation_Teststand/2_20_05_2021/sensor_positions.xlsx")
# =============================================================================

#%% get absolute path for the files 

# =============================================================================
# location = "C:/Users/Devineni/OneDrive - bwedu/6_Recirculation_Teststand/2_20_05_2021/excel data/"
# 
# abs_path = []
# 
# # r=>root, d=>directories, f=>files
# for r, d, f in os.walk(location):
#    for item in f:
#       if '.xlsx' in item:
#          abs_path.append(os.path.join(r, item))
# =============================================================================
#%%
# fig , ax = plt.subplots()

# =============================================================================
# df_list = []
# 
# for file in abs_path:
#         
#     df1 = pd.read_excel(file, skiprows = 1)
#     df1 = df1.iloc[:,[1,4]]
#     name = [sensor for sensor in sensor_list if sensor in file]
#     legends = pos.loc[pos["sensor"] == name[0],["legend"]].iat[0,0]
#     df1.columns = ["datetime", legends]
# 
#     print(df1.dtypes)
# 
#     df1 = df1.set_index("datetime")
#     # df1.plot(y = legends, ax = ax)
#     df_list.append(df1)
# =============================================================================
#%%

# =============================================================================
# co2_df = pd.concat(df_list, axis = 1)
# co2_df.to_excel("save1.xlsx")
# # co2_df = co2_df.iloc[:,[0,9,10,12]]
# =============================================================================
#%%
import plotly.io as pio

pio.renderers.default='browser'
pd.options.plotting.backend = "plotly"

import plotly.express as px

# df = px.data.stocks()
df2 = pd.read_excel("save1.xlsx")
df2 = df2[sorted(df2.columns)]
df3 = df2.fillna(0)

fig = px.line(df3, x="datetime", y=df3.columns, title='60 m3/hr (Thursday), 1) Entire AC closed loop and 2) Test stand closed loop')

fig.show()


import plotly.io as pio

pio.renderers.default='browser'
df2 = df2.set_index("datetime")



#%%

df2_1 = df2.truncate(before = "2021-05-20 17:59:31", after = "2021-05-20 18:15:15").reset_index()

fig = px.line(df2_1, x="datetime", y=df2_1.columns, title="Waiting time plot Day 2 Exp 2")

fig.show()


#%%
cols = df2_1.columns.to_list()
cols.remove("datetime")

df4 = pd.DataFrame({'serial':cols})
df4["slope"] = np.nan
df4["intercept"] = np.nan
df4["r_squared"] = np.nan
#%%
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.linear_model import LinearRegression


for i in cols:    
    X = df2_1.index.values.reshape(-1, 1)  # values converts it into a numpy array
    Y = df2_1[str(i)].values.reshape(-1, 1)  # -1 means that calculate the dimension of rows, but have 1 column
    model = LinearRegression()  # create object for the class
    model.fit(X, Y)  # perform linear regression
    Y_pred = model.predict(X)  # make predictions

    slope = float(model.coef_)
    intercept = float(model.intercept_)
    r_squared = float(model.score(X, Y))
    rmse = mean_squared_error(X, Y_pred)
    df4.loc[df4['serial'] == str(i),'slope'] = slope
    df4.loc[df4['serial'] == str(i),'intercept'] = intercept
    df4.loc[df4['serial'] == str(i),'r_squared'] = r_squared
    df4.loc[df4['serial'] == str(i),'rsme'] = rmse

df4.to_excel("reg_resuult_exp_2.xlsx")
prYellow("The slope results have been saved as reg_resuult_exp_2.xlsx")

#%%


df2_2 = df2.truncate(before = "2021-05-20 19:07:31", after = "2021-05-20 19:18:36").reset_index()

fig = px.line(df2_2, x="datetime", y=df2_2.columns, title="Waiting time plot Day 2 Exp 4")

fig.show()


#%%
cols = df2_2.columns.to_list()
cols.remove("datetime")

df5 = pd.DataFrame({'serial':cols})
df5["slope"] = np.nan
df5["intercept"] = np.nan
df5["r_squared"] = np.nan
#%%
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.linear_model import LinearRegression


for i in cols:    
    X = df2_2.index.values.reshape(-1, 1)  # values converts it into a numpy array
    Y = df2_2[str(i)].values.reshape(-1, 1)  # -1 means that calculate the dimension of rows, but have 1 column
    model = LinearRegression()  # create object for the class
    model.fit(X, Y)  # perform linear regression
    Y_pred = model.predict(X)  # make predictions

    slope = float(model.coef_)
    intercept = float(model.intercept_)
    r_squared = float(model.score(X, Y))
    rmse = mean_squared_error(X, Y_pred)
    df5.loc[df5['serial'] == str(i),'slope'] = slope
    df5.loc[df5['serial'] == str(i),'intercept'] = intercept
    df5.loc[df5['serial'] == str(i),'r_squared'] = r_squared
    df5.loc[df5['serial'] == str(i),'rsme'] = rmse

df5.to_excel("reg_resuult_exp_3.xlsx")
prYellow("The slope results have been saved as reg_resuult_exp_3.xlsx")














