#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 11:19:01 2024

@author: maximeb
"""

from rdflib import Graph
import pandas as pd

#%% import db of ontologies
file = 'ontology_set/20240308_ontologies_and_standards.csv'
df = pd.read_csv(file, sep=";").drop('id', axis= 1)

#%% Get list of ttl or rdf ontologies

mask =  df['url'].str.endswith('ttl', na=False) | df['url'].str.endswith('rdf', na=False)

df = df[mask].reset_index(drop=True)

d = df.to_dict('index')


#%%

for n in d:
    try:
        d[n]['graph']=Graph().parse(d[n]['url'])
        
    except:
        d[n]['graph']=Graph().parse(d[n]['url'], format='ttl')
    
#%%    

