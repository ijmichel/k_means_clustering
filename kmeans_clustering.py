#!/usr/bin/python

import re
import os

def kmeans(inputPath,K) :

    transactions = [] # list of all points wihout parse
    frequentKItems = {}
    totalLineCount = 0

    with open(inputPath) as f:
         for line in f:
            totalLineCount = totalLineCount + 1
            line = line.rstrip()
            data = re.split(',', line)
            transactions.append(data)
            print ("data --> ", data)
            for category in data:
                print ("cat -->", category)
                    
                    
kmeans("places.txt",3);