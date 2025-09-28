# simple-k-means
Naive K-Means implementation with basic visualization. The code presented here does the following:

-Generates n random points on a coordinate plane based on seed (rng) and basic function (rand)

-Initializes k random "centers" around which to begin the clustering

-Compares each point's distance from each center, and assigns it to the cluster that has the shortest distance from it:
    point p_i has the following distances from each of 5 clusters:
        distances(0) = 16.5
        distances(1) = 28.7
        distances(2) = 14.2
        distances(3) = 9.0
        distances(4) = 18.8
    distances(3) is the min of distances, therefore p_i is in cluster 3 (although in my implementation, I label the clusters from 1 to k. So technically it would be part of "Cluster 4".) It's accurate to say that the argmin(distances) for any point p_i is the cluster it will be assigned to.

-Reassign centers by averaging Euclidean distances between all points in that cluster, generating a new point to cluster around.
    If the average of points (calculated with np.mean()) produces a point that isn't in the data set, that point will be simply clustered around. 
    It however will be plotted if this is true after iteration (meaning technically you will see n+k total points plotted, not n points).
    So these "new points" that are generated don't in any way affect the pre-existing dataset.

-Repeat this process until centers do not change after an iteration.
    This works because if centers don't change after an iteration, it means the means of all points stayed the same (and likely that no points shifted clusters). This means we've "converged" to a solution. 
    With randomly initialized points, this clustering is typically somewhat accurate. But It isn't a perfect solution with more carefully-crafted datasets that are shaped into specified clusterings. For those datasets (and most datasets, honestly), you'd much rather use K-Means++, which has a much more robust center initialization method rather than just random.

About generating hex codes, I had the following code:
# hex_codes = []
# for i in range(k):
#     hex_codes.append('#'+chr(random.randint(65, 70))+chr(random.randint(65,70))+str(random.randint(1000,9999)))

This generated a string of a random hexadecimal color value to assign to my clusters. I actually decided to use this method because I was frustrated with the documentation on colormaps in matplotlib, so I figured I'd do it myself. But basically, this works by randomizing two capital letters as the first two characters in the hex value, then a 4-digit number from 1000-9999 as the next values.

#ff0000 is red, #000000 is black, #ffffff is white, #1fffff is turquoise, etc.

 There are way better ways to do this, as this range of colors is actually super limited. For example, I can't generate any turquiose hues because I only restrict myself to two letters in the randomization. I may come back to fix this in the future and apply it to other projects since it was pretty fun to come up with.

 Anyway feel free to test this code out. Adjust your parameters