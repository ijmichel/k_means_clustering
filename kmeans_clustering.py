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
            # print ("data -->",data)
            transactions.append(data)
    
    numPoints = len(transactions)
    
    x = np.array(transactions)
    
    indices = np.random.choice(x.shape[0], 3, replace=False)
    print ("Choices 3--> ", indices)

                    
kmeans("places.txt",3);