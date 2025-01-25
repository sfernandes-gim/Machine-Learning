''' Simple k means code to reflect the behaviour of the k means clustering algorithm'''

import random 
import numpy as np
np.random.seed(42)

#Create a Custom Class
class KMeans_Custom:
    
    X_Input=[] #Input Matrix
    centers =[] #Centroids
    cluster = () ## Various clusters
    k =0

    def __init__(self,X,k):
        self.X_Input = X
        self.k = k
        self.cluster= tuple(range(self.k))

    # Function to assign Random centers initally
    def assign_rand_centroid(self):
        for i in range(self.k):
            self.centers.append(self.X_Input[random.randrange(0,len(self.X_Input))])
      
    # Function to allocate the respective cluster number based on the distance of the point from centroid of each
    def cluster_allocation(self):
        temp_centers = []
        for row in self.X_Input:
            matrix_point = np.array([row for _ in range(self.k) ])
            temp_centers.append(self.cluster[np.argmin( np.sqrt(np.square(matrix_point -  np.array(self.centers)).sum(axis=1)))])
        return temp_centers
    
    # Function to recalculate new centroid based on new cluster assignments
    def recalculate_centroids(self,arr_clusters):

        new_centroids = []
       
        for i in self.cluster:
            bool_select = [True if elem == i else False for elem in arr_clusters ]
            new_centroids.append(list(self.X_Input[bool_select].sum(axis=0)/len(self.X_Input[bool_select]))) # Filter rows where cluster is ith cluster and need to take average as centroid

        self.centers=new_centroids


# Generate a random matrix as input
inp_raw = np.random.randint(1,21,size=(1000,3)) #Generate between 1 - 20 with 1000 rows and 3 colums

#No of clusters
k_center = 2
kmean_algo = KMeans_Custom(inp_raw,k_center)
kmean_algo.assign_rand_centroid()
arr_clus=kmean_algo.cluster_allocation()

#Iterate till convergence
for n in range(200):
    kmean_algo.recalculate_centroids(arr_clus)
    new_clusters=kmean_algo.cluster_allocation()
    if (arr_clus==new_clusters): #using cluster allocation as stopping criteria instead of the centroid
        break
    else:
        arr_clus = new_clusters


print(f'Iteration #n: ', n)
print(arr_clus[:5])

### Running Kmeans from Package

from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters=k_center, random_state=42, n_init='auto')
clusters = kmeans.fit_predict(inp_raw)

#Print("Automated k means")
print(clusters[:5])








