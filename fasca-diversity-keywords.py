#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  8 11:44:37 2025

@author: gustavo
"""

import glob
import pandas as pd
import re
import numpy as np
import matplotlib.pyplot as plt
from div import richness, shannon_diversty_index, dr_rate
from langdetect import detect


def plot_subject_diversity(host, language, df, column_name, years, r_scale=1):
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
    plt.title(f'Diversity of {name} ({host} {language})')
    plt.savefig(f'plots/{column_name}_{host}_{language}.png', dpi=300)
    
def split(s, separator):
    """
    Return all  tokens in the string after split by symbol s    

    Parameters
    ----------
    s : str
        input string.
    separator : str
        character used as separator.

    Returns
    -------
    list
        All tokens of length at least 2 after splitting s by separators.

    """
    #print(s)
    tokens = re.split('\s*' + separator + '\s*', s.strip())
    
    return list(filter(lambda t: len(t) > 1 , map(str.strip, tokens)))

def split_keyword(subject):
    """
    Parameters
    ----------
    subject : str
        Complete subject descriptor, such as Commerce--History
    Returns
    -------
    list of str
    Subdivisions (at least two characters long) in one subject, for example, 
    ['Commerce', 'History'].
    """
    tokens = re.split('\s*;\s*', subject.strip())

    return list(filter(lambda t: len(t) > 1 , map(str.strip, tokens)))

def extractKeywords(x):
    try:
        keywords = ""
        #print(x)
        for item in x:
            cleanText = item["text"].lower() # tolower 
            cleanText = cleanText.strip() # remove spaces begin-end
            cleanText = cleanText.replace(".","") # remove .
            cleanText = cleanText.replace('"','') # remove "
            cleanText = cleanText.replace(";","@") # change ; for new keywords
            cleanText = cleanText.replace(",","@") # change , for new keywords
            
            if not cleanText.startswith('http'):
                keywords += "@" + cleanText #+ "--" + item["lang"]
        return keywords
    except:
        return 0

def detect_language(x):
    try:
        return detect(x)
    except:
        return 0

def extract_data(path, language, create_log):

    json_files = glob.glob(path + "/*.json")
    print(json_files)
    
    df = pd.DataFrame()
    for file_path in json_files:
        print(file_path)
        df_file = pd.read_json(file_path) #'input/gotriple_response_11.json'
        df = pd.concat([df,df_file])

    df['keywords_extracted'] = df['keywords'].apply(extractKeywords) 

    df["year"] = df['date_published'].str.extract('(\d{4})', expand=True) 
    df["year"] = pd.to_numeric(df["year"])
    df.dropna(subset=["year"], inplace=True)
    print(df["year"].unique())

    df = df[(df.year!='')&(df.keywords_extracted.str.len() > 1)]
    df['keywords_extracted'] = df.keywords_extracted.apply(lambda s: split(s, '@'))
    df = df.explode('keywords_extracted')

    df = df[(df.keywords_extracted.str.len() > 1)]
    df['keywords_lang'] = df["keywords_extracted"].apply(lambda x: detect_language(x))

    if language != '':
        df = df[(df.keywords_lang == language)]
    print(df["keywords_lang"].unique())

    if create_log:
        df_keywords = df['keywords_extracted']
        df_keywords.to_csv(f'keywords_extracted_{language}.csv', index=False)
    
    return df


host="goTriple"
scale=1
first=1998
last=2020
create_log = True
language = "es"
path = 'input'

df = extract_data(path, language, create_log)
plot_subject_diversity(host, language, 
                        df, 
                        'keywords_extracted', 
                        range(first, last + 1),  
                        scale)

dfShannon = df[df.year.between(first,last)]
print('DR_RATE=', dr_rate(dfShannon.keywords_extracted))
