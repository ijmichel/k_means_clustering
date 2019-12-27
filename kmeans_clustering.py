#!/usr/bin/python

import re
import os
import math
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
    
    indices = np.random.choice(x.shape[0], K, replace=False)
    print ("Choices K--> ", indices)
    
    currentCentroids = []
    for n in range(K):
        print ("X --> ",n)
        currentCentroids.append(transactions[indices[n]])
        print ("Ponit X--> ", n, " : ", currentCentroids[n])
        
    pointCentroidIndex = {}

    for i,aPoint in enumerate(x):
        print ("aPoint", aPoint)
        leastDist = 99999
        Px = aPoint[0]
        Py = aPoint[1]
        for j,aCentroid in enumerate(currentCentroids):
            Cx = aCentroid[0]
            Cy = aCentroid[1]
            print (Px , ":",Py,":",Cx,":",Cy)
            currDistance = math.sqrt((float(Px) - float(Cx))**2 + (float(Py) - float(Cy))**2 )
            if currDistance < leastDist:
                leastDist = currDistance
                print ("i-->",i)
                pointCentroidIndex[i] = j
                print("point ", i, " Centroid --> ", currentCentroids[j])
                    
                    
kmeans("places.txt",3);