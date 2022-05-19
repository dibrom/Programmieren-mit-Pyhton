#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import sys

from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource
from bokeh.models.tools import HoverTool
from bokeh.io import output_notebook
from bokeh.layouts import gridplot


# In[2]:


class Value_functions():
    def quad_error(value_1, value_2):
        """
        This function gets two values, adds both and computes the quadratic error
 
        input arguments:
        - value_1: numeric
        - value_2: numeric 
 
        dependencies:
        - none
 
        output arguments:
        - output: numeric quadratic error of value_1 and value_2
        """
        output = pow((value_1-value_2),2)
        return output
    
    def euclidean_distance(x1, y1, x2, y2):
        """
        This function gets two pairs of values (x and y) and 
        computes the euclidean distance between both points in two dimensional area
 
        input arguments:
        - x1: numeric
        - x2: numeric 
        - x3: numeric 
        - x4: numeric 
 
        dependencies:
        - none
 
        output arguments:
        - euc_dist: numeric euclidean distance between (x1,y1) and (x2,y2)
        """
        euc_dist = ((x2-x1)**2+(y2-y1)**2)**(1/2)
        return euc_dist


# In[3]:


class Read_dataframe():
    def read_csv_to_dataframe(filepath):
        """
        This function gets a filepath and trys to read a csv file to pandas dataframe 
 
        input arguments:
        - filepath: string
 
        dependencies:
        - none
 
        output arguments:
        - df: pandas dataframe with csv content
        """
        try:
            df = pd.read_csv(filepath)
            return df
        except OSError as e:
            print(f"File {filepath} not found!", file=sys.stderr)


# In[4]:


class Fitting_function():
    def find_fitting_function(train_dataframe, ideal_dataframe, function_number):
        """
        This function gets two pandas dataframes and a number. The number decides wich function in the train 
        dataframe is compared to all functions in ideal dataframe.
        
        input arguments:
        - train_dataframe: pandas dataframe
        - ideal_dataframe: pandas dataframe
        - function_number: int
        
        dependencies:
        - none
 
        output arguments:
        - ideal_function_train: number which defines the fitting function of the ideal dataset
        """
        train_ideal_df = pd.DataFrame({'X (Test Funktion)':np.arange(-20,20,0.1)})
        for i in range(1,len(ideal_dataframe.columns),1):
            train_ideal_df[str(i)] = 0.0
        for i in range(0,len(ideal_dataframe),1):
            for j in counter:
                train_value = train_dataframe.iloc[i,function_number] #Train dataset function 1
                ideal_value = ideal_dataframe.iloc[i,j]
                train_ideal_df.iat[i,j] = Value_functions.quad_error(train_value,ideal_value)
        train_ideal = train_ideal_df.apply(np.sum, axis=0)#.to_frame()
        train_ideal_min = train_ideal.drop(labels=['X (Test Funktion)']).min()
        ideal_function_train = train_ideal[train_ideal == train_ideal_min].index[0]
        return ideal_function_train


# In[5]:


# Class to have inheritance
class Fitting_Function_ideal(Fitting_function):
    None


# In[ ]:


class Visualize_data():
    def vis_train_ideal(train_dataframe, ideal_dataframe, train_function, ideal_function_train):
        """
        This Function gets two dataframes, and two integers. Both dataframes contain functions which are to displayed.
        The integers define which of these functions are visualized with bokeh library

        input arguments:
        - train_dataframe: pandas dataframe
        - ideal_dataframe: pandas dataframe
        - train_function: int
        - ideal_function_train: int

        dependencies:
        - none

        output arguments:
        - none - direct output for further computing but a bokeh graph
        """
        train_ideal_function_plot = figure()
        train_ideal_function_plot.circle(x="X",y="Y" + str(train_function) +" (Training Funktion)",                                    source = train_dataframe, size = 5, color='green', legend_label="Train Y" +                                          str(train_function))
        train_ideal_function_plot.circle(x="X (Test Funktion)",y="Y" + ideal_function_train + " (Ideale Funktion)",                                    source = ideal_dataframe, size = 1, color='blue', legend_label="Ideal Y" +                                          ideal_function_train)
        train_ideal_function_plot.title.text = "Train Data Y" + str(train_function) + " - ideal Data Y" +         ideal_function_train
        train_ideal_function_plot.xaxis.axis_label = "x"
        train_ideal_function_plot.yaxis.axis_label = "y"
        show(train_ideal_function_plot)
        
    def vis_train_ideal_in_nb(train_dataframe, ideal_dataframe, train_function, ideal_function_train):
        """
        This Function gets two dataframes, and two integers. Both dataframes contain functions which are to displayed.
        The integers define which of these functions are visualized with bokeh library

        input arguments:
        - train_dataframe: pandas dataframe
        - ideal_dataframe: pandas dataframe
        - train_function: int
        - ideal_function_train: int

        dependencies:
        - none

        output arguments:
        - none - direct output for further computing but a bokeh graph in seperate tab
        """
        train_ideal_function_plot = figure()
        train_ideal_function_plot.circle(x="X",y="Y" + str(train_function) +" (Training Funktion)",                                    source = train_dataframe, size = 5, color='green', legend_label="Train Y" + str(train_function))
        train_ideal_function_plot.circle(x="X (Test Funktion)",y="Y" + ideal_function_train + " (Ideale Funktion)",                                    source = ideal_dataframe, size = 1, color='blue', legend_label="Ideal Y" + ideal_function_train)
        train_ideal_function_plot.title.text = "Train Data Y" + str(train_function) + " - ideal Data Y" + ideal_function_train
        train_ideal_function_plot.xaxis.axis_label = "x"
        train_ideal_function_plot.yaxis.axis_label = "y"
        output_notebook()
        show(train_ideal_function_plot)


# In[ ]:




