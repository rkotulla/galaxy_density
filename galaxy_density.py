#!/usr/bin/env python

import os
import sys
import numpy




if __name__ == "__main__":

    filename = sys.argv[1]

    mag_column = int(sys.argv[2])

    distance_limit = float(sys.argv[3]) # given in arcmins

    mag_range = float(sys.argv[4])


    data = numpy.loadtxt(filename)
    #print data.shape

    ra = data[:,0]
    dec = data[:,1]

    galaxy_magnitude = data[:, mag_column]

    results = []
    for i_gal in range(data.shape[0]):

        distance = numpy.hypot(
            data[i_gal,1] - data[:,1],
            (data[i_gal,0] - data[:,0])*numpy.cos(numpy.radians(data[i_gal,1]))
        )
        #print distance.shape

        #
        # calculate the number of other galaxies within the distance_limit
        # subtract 1 as each galaxy has a distance of 0 to itself
        #
        n_nearby = numpy.sum( distance < distance_limit/60. ) - 1

        #
        # now find the distance to the closest other galaxy with a magnitude
        # of mag_range to this galaxy
        #
        mag_within_range = galaxy_magnitude < (galaxy_magnitude[i_gal]+mag_range)
        sort_by_distance = numpy.argsort(distance)
        closest_neighbor = distance[sort_by_distance][1]

        print i_gal, data[i_gal,0], data[i_gal,1], n_nearby, closest_neighbor
        results.append([i_gal, data[i_gal,0], data[i_gal,1], n_nearby, closest_neighbor])

    results = numpy.array(results)
    numpy.savetxt("results.txt", results)




