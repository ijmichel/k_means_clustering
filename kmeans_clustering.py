#!/usr/bin/python

import re
import os
import numpy as np

def kmeans(inputPath,K) :

    transactions = [] # list of all points wihout parse

    with open(inputPath) as f:
         for line in f:
            line = line.rstrip()
            data = re.split(',', line)
            print ("data -->",data)
            transactions.append(data)
    
    numPoints = len(transactions)
    

                    
kmeans("places.txt",3);