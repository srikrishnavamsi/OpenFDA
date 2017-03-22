#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 17:58:51 2017

@author: Sri
"""

import urllib2 as ulib
import json as js
import simplejson
import ssl
import requests



def get_data(url):
    """
    Simple funtion to read the data from OpenFDA api call and return a list of 
    meta data and results
    
    """
    
    request_string = url    
    r=requests.get(request_string)
    data = r.json()   
    #print data.keys()
    meta, results = data["meta"], data["results"]
    
    return [meta, results]


def main():

    print "this is a simple function to get data"
    
if __name__ == "__main__":
    main()
    
    