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
        # print ("X --> ",n)
        currentCentroids.append(transactions[indices[n]])
        print ("Centroid -> ", n, " : ", currentCentroids[n])
        
    pointCentroidIndex = {}
 
    calculateClosestCentroid(x,pointCentroidIndex,currentCentroids)
    
    f = open("clusters.txt", "w")
    for index in pointCentroidIndex:
        tWrite = str(index) +  " " + str(pointCentroidIndex[index]) + "\n"
        f.write(tWrite)
    f.close()
    
    print("DONE!")
    
        
def updateCentroidCoordinates(x,pointCentroidIndex,currentCentroids) :
    centroidIndexToNewCoords = {}
    for i,aPoint in enumerate(x):
        # print ("i-->",i)
        if pointCentroidIndex[i] in centroidIndexToNewCoords:
            coordsForNewCentroid = centroidIndexToNewCoords[pointCentroidIndex[i]]
            coordsForNewCentroid.append(aPoint)
            centroidIndexToNewCoords[pointCentroidIndex[i]] = coordsForNewCentroid
        else:
            coordsForNewCentroid = []
            coordsForNewCentroid.append(aPoint)
            centroidIndexToNewCoords[pointCentroidIndex[i]] = coordsForNewCentroid
            
    for aCentIndex in centroidIndexToNewCoords.keys():
        coordsForNewCentroid = centroidIndexToNewCoords[aCentIndex]
        data =  np.array(coordsForNewCentroid).astype(np.float)
        averaged = np.average(data, axis=0)
        currentCentroids[aCentIndex] = averaged
        print ("Averaged--> Key", aCentIndex, "Averaged-->",averaged)
        
            
     
def calculateClosestCentroid(x,pointCentroidIndex,currentCentroids) :
     inProgressPointCentroidIndex = {}
     aCentroidChanged = False
     for i,aPoint in enumerate(x):
        # print ("aPoint", aPoint)
        leastDist = 99999
        Px = aPoint[0]
        Py = aPoint[1]
        for j,aCentroid in enumerate(currentCentroids):
            Cx = aCentroid[0]
            Cy = aCentroid[1]
            # print (Px , ":",Py,":",Cx,":",Cy)
            currDistance = math.sqrt((float(Px) - float(Cx))**2 + (float(Py) - float(Cy))**2 )
            if currDistance < leastDist:
                leastDist = currDistance
                inProgressPointCentroidIndex[i] = j
                # print("point ", i, " Centroid --> ", currentCentroids[j], "Distance-->",leastDist,"Centroid-->",pointCentroidIndex[i])   

     for c1 in inProgressPointCentroidIndex.keys() :
         if c1 in pointCentroidIndex:
             if inProgressPointCentroidIndex[c1] is not pointCentroidIndex[c1]:
                aCentroidChanged = True
         else:
             aCentroidChanged = True
             
         pointCentroidIndex[c1] = inProgressPointCentroidIndex[c1]
     
     if aCentroidChanged is True:
        updateCentroidCoordinates(x,pointCentroidIndex,currentCentroids)
        calculateClosestCentroid(x,pointCentroidIndex,currentCentroids)
                    
kmeans("places.txt",3);