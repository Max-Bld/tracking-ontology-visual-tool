#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 11:19:01 2024

@author: maximeb
"""

from rdflib import Graph
import pandas as pd
import requests
import re
from functions import extract_ttl_prefixes

#%% import db of ontologies
file = 'ontology_set/20240308_ontologies_and_standards.csv'

df = pd.read_csv(file, sep=";").drop('id', axis= 1)

#%% Data Cleaning

mask =  df['url'].str.endswith('ttl', na=False)
df.loc[mask, 'syntax'] = 'ttl'

mask =  df['url'].str   .endswith('rdf', na=False)
df.loc[mask, 'syntax'] = 'rdf'

#%% Get list of ttl or rdf ontologies

mask =  df['url'].str.endswith('ttl', na=False) | df['url'].str.endswith('rdf', na=False)

df = df[mask].reset_index(drop=True)

d = df.to_dict('index')

#%% retrieve the related ontologies to the current ontology
for ontology in d:
    ontology_file = requests.get(d[ontology]['url']).text
    
    if d[ontology]['syntax']=='ttl':
        list_of_prefixes = extract_ttl_prefixes(ontology_file)
        
        d[ontology]['linked_ontologies']=list_of_prefixes
        

#%% Visualize the relations between ontologies
#%% Add graphs

for n in d:
    try:
        d[n]['graph']=Graph().parse(d[n]['url'])
        
    except:
        d[n]['graph']=Graph().parse(d[n]['url'], format='ttl')

#%% Graph manipulation

g = d[0]['graph']

for s, p, o in g:
    print((s, p, o))