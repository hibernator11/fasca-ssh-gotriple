#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  8 11:44:37 2025

@author: gustavo
"""

import glob
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from div import richness, shannon_diversty_index, dr_rate

def plot_subject_diversity(host, df, column_name, years, r_scale=1):
    """
    Create cummulative plot for the specified data, range of years 
    Parameters
    ----------
    host : str
        Host institution short name, to be used in the plot title.
    df : DataFrame
        DataFrame with columns YEAR and column_name.
    years : iterable collection of int
        The years to be used as X-points for the plot
    r_scale : int, optional
        Scale for the reduction of richness. The default is 1.
    """
    plt.clf()
    X = np.array(years)
    R = list()  # richness
    D = list()  # diversity
    for year in X:
        print(year)
        values = df[df.year <= year][column_name]
        #R.append(richness(values) / r_scale)
        #D.append(shannon_diversty_index(values))
        if len(values) != 0:
            R.append(richness(values) / r_scale)
            D.append(shannon_diversty_index(values))
        else: 
            X = np.delete(X, np.where(X==year)[0][0])
    if r_scale == 1:
        plt.plot(X, R, 's', label='richness')
    else: 
        plt.plot(X, R, 's', label=f'richness / {r_scale}')
    plt.plot(X, D, 'o', label='diversity')
    
    plt.legend(loc='upper left')
    plt.grid()
    xticks = [x for x in range(min(X), max(X) + 1) if x % 5 == 0]
    plt.xticks(xticks, xticks)
    _, yhigh = plt.ylim()
    plt.ylim(0, 1.1 * yhigh)
    name =  column_name.lower().replace('_', ' ')
    plt.title(f'Diversity of {name} ({host})')
    plt.savefig(f'plots/{column_name}_{host}.png', dpi=300)
    

def extract_data(path, create_log):

    json_files = glob.glob(path + "/*.json")
    print(json_files)
    
    df = pd.DataFrame()
    for file_path in json_files:
        print(file_path)
        df_file = pd.read_json(file_path) #'input/gotriple_response_11.json'
        df = pd.concat([df,df_file])

    #df['keywords_extracted'] = df['keywords'].apply(extractKeywords) 

    df["year"] = df['date_published'].str.extract('(\d{4})', expand=True) 
    df["year"] = pd.to_numeric(df["year"])

    df = df[(df.year!='')&(df.in_language.str.len() > 1)]
    df = df.explode('in_language')

    df = df[(df.in_language.str.len() > 1)]
    
    if create_log:
        df_keywords = df['in_language']
        df_keywords.to_csv('languages.csv', index=False)
    
    return df


host="goTriple"
scale=1
first=1998
last=2020
create_log = True
path = 'input'

df = extract_data(path, create_log)
plot_subject_diversity(host,  
                        df, 
                        'in_language', 
                        range(first, last + 1),  
                        scale)

print('DR_RATE=', dr_rate(df.in_language))

