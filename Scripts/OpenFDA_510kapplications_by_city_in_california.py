# !/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 18:05:46 2017

@author: Sri
"""

import urllib2 as ulib
import json as js

import matplotlib.pyplot as plt
import numpy as np

from operator import itemgetter
import pandas 
import matplotlib.pyplot as plt
from GetData import get_data


def clearances_by_class():
    api_call = "https://api.fda.gov/device/510k.json?search=medical_specialty_description:ophthalmic&count=device_class"
    data = get_data(api_call)
    data_f = pandas.DataFrame(data[1])
    data_f = data_f.rename(columns={"count":"number of 510(k) clearances", "term": "device class"})
    print data_f
    data_f.to_csv("../510(k) clearances by class.csv")

def clearances_by_product_code():
    pass


def main():
    ##################
    # api call for number of 510(k) applications by city in California  
    #url = "https://api.fda.gov/device/510k.json?search=medical_specialty_description:ophthalmic+AND+state:ca&count=city"
    
    clearances_by_class() 
    

    
if __name__ == "__main__":
    main()