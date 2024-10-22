

"""
Solutions to module 4
Review date:
"""

student = "Marta Carvalho"
reviewer = ""

import math as m
import random as r
import numpy as np

def sphere_volume(n, d):
    # n is a list of set of coordinates
    # d is the number of dimensions of the sphere 
    
    # Create n lists for coordinates of points in d-dimention, using list compressions
    # Points are bound to hypercube where each side has length 2, with the point (0,0) at its center
    coordinates = [np.random.uniform(-1,1,d) for i in range(n) ]
    
    # Create a list of the sum of the squares of the coordinates for each generated point
    # Uses the map() function
    squared_coordinates = map(lambda point: sum(x*x for x in point), coordinates)
    
    # Selects the points inside the hypersphere
    # Uses the filter() function
    points_inside = list(filter(lambda x: x<=1, squared_coordinates))
    
    # Ammount of points inside the sphere
    ns = len(points_inside)
    
    # Returns the approximate volume with: Vs/Vc=ns/nc, with nc=n and Vc=2**d
    return (ns/n)*2**d

def hypersphere_exact(n,d):
    return m.pi**(d/2)/m.gamma(d/2+1)
     
def main():
    
    print('Approximate volume of the hypersphere in d=2: ', sphere_volume(100000,2), '\nExact volume: ', hypersphere_exact(100000,2))
    print('Approximate volume of the hypersphere in d=11: ', sphere_volume(100000,11), '\nExact volume: ', hypersphere_exact(100000,11))

if __name__ == '__main__':
	main()
