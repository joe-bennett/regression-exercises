
import numpy as np
import pandas as pd
import seaborn as sns
import wrangle
import matplotlib.pyplot as plt


def plot_variable_pairs(df):
    '''this function takes in data and displays all pairwise relationships and adds regression line'''
    
    sns.pairplot(data=df.drop(columns='fips'),kind='reg',plot_kws={'line_kws':{'color':'red'}}, corner=True)
    plt.show()        




def plot_catagorical_and_continous_vars(df,x,y):
    '''takes in dataframe, followed by x value then y value to compare a catagorical and continous variable threed different ways
    stripplot, boxplot, and catplot'''
    sns.stripplot(x=x,y=y,data=df)
    plt.show()
    sns.boxplot(x=x,y=y,data=df)
    plt.show()
    sns.catplot(x=x,y=y,data=df)
    plt.show()
        