#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 15:16:03 2024

@author: maximeb
"""

import re

def extract_ttl_prefixes(ontology_file):
    """
    

    Parameters
    ----------
    ontology_file : .ttl 
        ontology turtle file

    Returns
    -------
    list_of_prefixes : list
        list of the URI dereferenced by the prefixes used in the ontology

    """
    list_of_prefixes = re.split('prefix', ontology_file, flags=re.IGNORECASE)
    list_of_prefixes.pop(0)
    
    for n in range(len(list_of_prefixes)):
        list_of_prefixes[n] = list_of_prefixes[n].split('<', maxsplit=1)[1]
        list_of_prefixes[n] = list_of_prefixes[n].split('>', maxsplit=1)[0]
        
        
    return list_of_prefixes