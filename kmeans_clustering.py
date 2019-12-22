#!/usr/bin/python

import re
import os

def kmeans(inputPath,K) :

    transactions = [] # list of all points wihout parse

    with open(inputPath) as f:
         for line in f:
            line = line.rstrip()
            data = re.split(',', line)
            transactions.append(data)
    
    numPoints = len(transactions)
    
                    
kmeans("places.txt",3);