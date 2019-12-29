# Description
This code takes in a list of coordinates and picks K of them at random.  The K coordinates are called centroids.   Then, it iterates through all the coordinates seeing how close they are each to the K ones picked.   The Kth point closest to each is associated to each point, which forms a cluster of coordinates around each K.   The X/Y coorindates of each of coordinates in each cluster are then avereages to find the new centroid locations.   The same process is repeated until each coordinate does not change it's centroid to another one.  

# Algorithm Steps
The algorithm for K-means involves the following steps:
- Step 1: Find the Euclidian distance between the centroids and each point.
- Step 2: Designate one centroid to each point which is the centroid closest to that point (minimum distance) Step 3: Calculate the mean of x1 and x2 of each data point in a class of centroids
- Step 4: Use the new means as the new centroid x1,x2
- Step 5: Go to Step 1 until the data points do not change their centroid class

#Formulas
Euclidean distance is: 
L2 =  sqrt(x1 − xcentroidx1 ^)2 + (x2 − xcentroidx2 )^2


# How to Use

- Change the places.text with your coordinates
- Run the code by running kmeans_clustering.py (built on Python 3.6)
- The output file will include the centroid #.
- NOTE: See the console for the coordinates of each of the K centroids after iterations are complete.  They are not ouput into the file.

# NOTES
- I used cloud9 (https://console.aws.amazon.com/cloud9/) on AWS to do the coding instead of a local IDE just to try it out, and then also tried out GitHub pages which I've never used before here to document by cloud9 experience:   https://ijmichel.github.io/k_means_clustering/
