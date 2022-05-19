#!/usr/bin/env python
# coding: utf-8

# In[1]:


# sql alchemy for database connection
import sqlalchemy as db
from sqlalchemy import inspect
from sqlalchemy.orm import sessionmaker

import os

# pandas for data handling
import pandas as pd
# numpy for numerical computing
import numpy as np

#import cryptography

from dotenv import load_dotenv

from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource
from bokeh.models.tools import HoverTool
from bokeh.io import output_notebook
from bokeh.layouts import gridplot

# Import other ipynb files
import import_ipynb
import functions as fn
from functions import Fitting_Function_ideal


# In[2]:


# Code excample from study script
# load environment variables
load_dotenv('credentials.env')
# create engine object
sql_password = os.getenv('MYSQL_PASSWORD')
con_str = "mysql+pymysql://root:" + sql_password + "@127.0.0.1:3306/pmp"
engine = db.create_engine(con_str,                           #echo = True
                         )

# create database connection
connection = engine.connect()


# In[3]:


# Get all table names from database
insp = inspect(engine)
print(insp.get_table_names())


# ### import train data from csv file

# In[4]:


# Load train data to dataframe
train_df = fn.Read_Dataframe.read_csv_to_dataframe('datasets/train.csv')
#train_df


# In[5]:


# Rename columns of train_df
train_df = train_df.rename(columns={"x": "X", "y1": "Y1 (Training Funktion)", "y2":"Y2 (Training Funktion)",                                    "y3":"Y3 (Training Funktion)", "y4":"Y4 (Training Funktion)"})


# #### Write data to mysql database

# In[6]:


# write train data from df to table
train_df.to_sql(
    'traindata',
    con=connection,
    if_exists='append',
    index=False,
    dtype={
        "X": db.Float,
        "Y1 (Training Funktion)	": db.Float,
        "Y2 (Training Funktion)	": db.Float,
        "Y3 (Training Funktion)	": db.Float,
        "Y4 (Training Funktion)": db.Float,
    }    )


# ### import ideal data from csv file

# In[7]:


# create counter to use for assigning 50 columns
counter = range(1,51,1)


# In[8]:


# Load ideal data to dataframe
ideal_df = fn.Read_Dataframe.read_csv_to_dataframe('datasets/ideal.csv')


# In[9]:


# sort ascending by x
ideal_df.sort_values(by = ["x"], ascending=True,                                     inplace=True, ignore_index=True)
ideal_df.head()


# In[10]:


# rename columns of ideal_df to match db column names
ideal_df = ideal_df.rename(columns={"x": "X (Test Funktion)"})    
for i in counter:
    ideal_df = ideal_df.rename(columns={"y"+str(i): "Y"+str(i)+" (Ideale Funktion)"})        
#ideal_df.head()


# #### Write data to mysql database

# In[11]:


# Create dictionary with column name and column data type for uploading data to my sql db 
columnsInput={
        "X (Test Funktion)": db.Float,
    }
for i in counter:
    columnsInput["Y"+str(i)+" (Ideale Funktion)"] = db.Float


# In[12]:


# Write data from dataframe to mysql db
ideal_df.to_sql(
    'idealdata',
    con=connection,
    if_exists='append',
    index=False,
    dtype = columnsInput
)


# ## Excersice 1

# ### Visualizing data

# ####  Train data

# In[13]:


# Plotting train data by using bokeh scatter plot and pandas datafragem
train_plot = figure()
train_plot.circle(x="X",y="Y1 (Training Funktion)", source = train_df, size = 3, color='green', legend_label="y1")
train_plot.circle(x="X",y="Y2 (Training Funktion)", source = train_df, size = 3, color='blue', legend_label="y2")
train_plot.circle(x="X",y="Y3 (Training Funktion)", source = train_df, size = 3, color='yellow', legend_label="y3")
train_plot.circle(x="X",y="Y4 (Training Funktion)", source = train_df, size = 3, color='red', legend_label="y4")
train_plot.title.text = "Train data"
train_plot.xaxis.axis_label = "x"
train_plot.yaxis.axis_label = "y"
show(train_plot)


# #### Ideal data

# In[14]:


# Plotting ideal data by using bokeh scatter plot and pandas datafragem
# because of the many columns I'm using a gridplot which is prepared within a for loop
figure_list = []
for i in counter:
    ideal_plot = figure()
    ideal_plot.circle(x="X (Test Funktion)",y="Y"+str(i)+" (Ideale Funktion)", source = ideal_df, size = 3, color='black')
    ideal_plot.title.text = "y"+str(i)
    ideal_plot.xaxis.axis_label = "x"
    ideal_plot.yaxis.axis_label = "y"+str(i)
    figure_list.append(ideal_plot)
grid = gridplot(figure_list, ncols=5,width=250, height=250)
show(grid)


# ### Check ideal function for train data function y1

# In[15]:


ideal_function_train_y1 = fn.Fitting_Function_ideal.find_fitting_function(train_df, ideal_df ,1)


# In[16]:


fn.Visualize_data.vis_train_ideal(train_df, ideal_df, 1, ideal_function_train_y1)


# ### Check ideal function for train data function y2

# In[17]:


ideal_function_train_y2 = fn.Fitting_Function_ideal.find_fitting_function(train_df, ideal_df ,2)


# In[18]:


fn.Visualize_data.vis_train_ideal(train_df, ideal_df, 2, ideal_function_train_y2)


# ### Check ideal function for train data function y3

# In[19]:


ideal_function_train_y3 = fn.Fitting_Function_ideal.find_fitting_function(train_df, ideal_df ,3)


# In[20]:


fn.Visualize_data.vis_train_ideal(train_df, ideal_df, 3, ideal_function_train_y3)


# ### Check ideal function for train data function y4

# In[21]:


ideal_function_train_y4 = fn.Fitting_Function_ideal.find_fitting_function(train_df, ideal_df ,4)


# In[22]:


fn.Visualize_data.vis_train_ideal(train_df, ideal_df, 4, ideal_function_train_y4)


# ## Excersize 2

# In[23]:


# Load test data to dataframe
test_df = fn.Read_Dataframe.read_csv_to_dataframe('datasets/test.csv')
test_df.sort_values(by = ["x"], ascending=True,                                     inplace=True, ignore_index=True)


# In[24]:


# Add columns to test_df and rename columns x and y
test_df = test_df.rename(columns={"x": "X (Test Funktion)", "y": "Y1 (Test Funktion)"})
test_df["Delta Y (Abweichung)"] = 0
test_df["Nummer der idealen Funktion"] = "No ideal function found"


# In[25]:


# Visualizing data
# Plotting test data by using bokeh scatter plot and pandas datafragem
test_plot = figure()
test_plot.circle(x="X (Test Funktion)",y="Y1 (Test Funktion)", source = test_df, size = 10, color='green')
test_plot.title.text = "Test data"
test_plot.xaxis.axis_label = "x"
test_plot.yaxis.axis_label = "y"
show(test_plot)


# In[26]:


# Create Dataset with fitting ideal functions
ideal_fitting_df = ideal_df[["X (Test Funktion)"
                             ,"Y"+ideal_function_train_y1+" (Ideale Funktion)"
                             ,"Y"+ideal_function_train_y2+" (Ideale Funktion)"
                             ,"Y"+ideal_function_train_y3+" (Ideale Funktion)"
                             ,"Y"+ideal_function_train_y4+" (Ideale Funktion)"]].copy()


# In[27]:


# Find fitting functions for test data
ideal_fitting_headers = list(ideal_fitting_df)
for i in range(0,len(test_df),1):
    test_x = test_df.iloc[i,0]
    test_y = test_df.iloc[i,1]
    y_delta = test_df.iloc[i,2]
    funct_numb = test_df.iloc[i,3]
    for j in range(0,len(ideal_fitting_df),1):
        ideal_x = ideal_fitting_df.iloc[j,0]
        if test_x == ideal_x:
            for k in range(1,len(ideal_fitting_df.columns),1):
                ideal_y = ideal_fitting_df.iloc[j,k]
                delta = test_y - ideal_y
                delta_abs = abs(test_y - ideal_y)
                if delta_abs < (2**(1/2)):
                    if funct_numb == "No ideal function found" or delta_abs < abs(y_delta):
                        y_delta = delta
                        test_df.iat[i,2] = delta
                        test_df.iat[i,3] = ideal_fitting_headers[k]


# In[28]:


# Create new dataset for visualization
test_df_vis = test_df[["X (Test Funktion)"
                             ,"Y1 (Test Funktion)"
                             ,"Delta Y (Abweichung)"]].copy()
test_df_vis["Y1 (Test Funktion) + Delta"] = test_df_vis["Y1 (Test Funktion)"] + test_df_vis["Delta Y (Abweichung)"]


# In[29]:


# Visualize test data and found ideal points from ideal functions
test_delta_plot = figure()
test_delta_plot.circle(x="X (Test Funktion)",y="Y1 (Test Funktion)", source = test_df_vis,                        size = 6, color='black', legend_label="Y1 (Test Funktion)")
test_delta_plot.circle(x="X (Test Funktion)",y="Y1 (Test Funktion) + Delta", source = test_df_vis,                        size = 3, color='red', legend_label="Y1 + Delta")
test_delta_plot.title.text = "Test data and test data + delta"
test_delta_plot.xaxis.axis_label = "x"
test_delta_plot.yaxis.axis_label = "y"
show(test_delta_plot)


# In[30]:


# write test data from df to table
test_df.to_sql(
    'testdata',
    con=connection,
    if_exists='append',
    index=False,
    dtype={
        "X (Test Funktion)": db.Float,
        "Y1 (Test Funktion)": db.Float,
        "Delta Y (Abweichung)": db.Float,
        "Nummer der idealen Funktion": db.String,
    }    )

