import numpy as np
import matplotlib.colors as mcolors
import matplotlib.pyplot as plt
import math
import random

# randomize function; this is how we generate random values. You
# can customize this function to generate data of different shapes.
# Right now the formula is quite basic.
def rand(x):
    return (random.random()+x)**2

# wrapper function to calculate Euclidean distance between two points.
# cleans up the code this way.
def euclidean(x, y):
    return np.linalg.norm(x-y, ord=2)**2
    

# declare the variables + their use:
# rng - the seed that affects the rand() function
# data - a 2d-array that holds all of our x-y point pairs
# n - the number of points
# k - the number of clusters
# centers - an array that holds our current center points for our clusters
# prev_centers - an array that holds the cluster centers from the previous iteration
# distances - temp array that holds the distances from a point to all clusters
# clusters - uneven 2d-array that holds all clusters

# adjust these top 3 parameters to change the plot
rng = 1
n = 100
k = 6
data = []
centers = []
prev_centers = []
distances = np.zeros(k)
clusters = []

# #generate hex codes for plot (optional, explained in readme)
# hex_codes = []
# for i in range(k):
#     hex_codes.append('#'+chr(random.randint(65, 70))+chr(random.randint(65,70))+str(random.randint(1000,9999)))

hex_codes = list(mcolors.cnames.values())[15:k+15]

#generate data points using basic rng seed
for i in range(n):
    data.append(np.array([rand(rng), rand(rng)]))

#print(data) # uncomment to see your points in output

 #pick k random centers (this is just standard k-means not ++)
centers = random.sample(data,k)

#initialize clusters
for i in range(k):
    clusters.append([])

while not(np.array_equal(prev_centers, centers)):
    #empty clusters, specify centers
    for i in range(k):
        clusters[i]=[]
    prev_centers = np.copy(centers)
    for i in range(n):
        for j in range(k):
            #measure distances between points and centers, pick the lowest one
            distances[j] = euclidean(data[i], centers[j])
        #assign points to clusters
        clusters[np.argmin(distances)].append(data[i])
    #reassign centers
    for i in range(k):
        centers[i] = np.mean(clusters[i], axis=0)


#plot points, including centers
for i in range(k):
    #uncomment below to see clusters listed at the end of iteration
    #print("Cluster number "+str(i+1)+": "+str(clusters[i]))

    #we will plot our centers here, label them, and assign colors to our clusters
    plt.scatter(centers[i][0], centers[i][1], c=hex_codes[i])
    plt.annotate("Center "+str(i+1), (centers[i][0], centers[i][1]), textcoords="offset points", xytext=(0, 10), ha='center')
    for j in range(len(clusters[i])):
        plt.scatter(clusters[i][j][0], clusters[i][j][1], c=hex_codes[i])



plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("k-means clustering")
plt.show()
