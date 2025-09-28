import numpy as np
import matplotlib.colors as mcolors
import matplotlib.pyplot as plt
import math
import random

def rand(x):
    return (random.random())+1

def euclidean(x, y):
    return np.linalg.norm(x-y, ord=2)**2
    

rng = 1
data = []
n = 100
epsilon = 15
k = 6
centers = []
prev_centers = []
distances = np.zeros(k)
clusters = []

# #generate hex codes for plot
# hex_codes = []
# for i in range(k):
#     hex_codes.append('#'+chr(random.randint(65, 70))+chr(random.randint(65,70))+str(random.randint(1000,9999)))

hex_codes = list(mcolors.cnames.values())[15:k+15]

#generate data
for i in range(n):
    data.append(np.array([rand(rng), rand(rng)]))

#print(data)

 #pick k random centers
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
    #print("Cluster number "+str(i+1)+": "+str(clusters[i]))

    #we will plot our centers here
    plt.scatter(centers[i][0], centers[i][1], c=hex_codes[i])
    plt.annotate("Center "+str(i+1), (centers[i][0], centers[i][1]), textcoords="offset points", xytext=(0, 10), ha='center')
    for j in range(len(clusters[i])):
        plt.scatter(clusters[i][j][0], clusters[i][j][1], c=hex_codes[i])



plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("k-means clustering")
plt.show()
