
"""
Solutions to module 4
Review date:
"""

student = ""
reviewer = ""

import math as m
from platform import processor
import random as r
import numpy as np
import concurrent.futures as future
from time import perf_counter as pc
from time import sleep as pause
import multiprocessing as mp


def sphere_volume(n, d):
    
    coordinates = [np.random.uniform(-1,1,d) for i in range(n) ]
   
    squared_coordinates = map(lambda point: sum(x*x for x in point), coordinates)
   
    points_inside = list(filter(lambda x: x<=1, squared_coordinates))
    
    ns = len(points_inside)
    
    return (ns/n)*2**d


def hypersphere_exact(n,d):
    return m.pi**(d/2)/m.gamma(d/2+1)

# parallel code - parallelize for loop
def sphere_volume_parallel1(n,d,np):
     #using multiprocessor to perform 10 iterations of volume function  
     
     with future.ProcessPoolExecutor() as ex:
         ps = [ex.submit(sphere_volume, n, d) for _ in range(np)]
         #  List of results for each future object: 
         results = [p.result() for p in ps]
         
     return sum(results)/len(results)
 

# parallel code - parallelize actual computations by splitting data
def sphere_volume_parallel2(n,d,np):
    #   Determines the size of np equal sets of points from n 
    
    sample_size = n//np
    """ with future.ProcessPoolExecutor() as ex:
        #   Applies the function to np chunks of data created.
        ps = [ex.submit(sphere_volume, sample_size, d) for _ in range(np)]
        results = [p.result() for p in ps]
        
    return sum(results)/len(results) """
    with future.ProcessPoolExecutor() as ex:
        results = ex.map(sphere_volume, [sample_size for _ in range(np)], [d for _ in range(np)])
    results = list(results)
    
    return sum(results)/len(results)
    
     
def main():
    # part 1 -- parallelization of a for loop among 10 processes 
    n = 100000
    d = 11
    np = 10

    print(f"Exact volume: {hypersphere_exact(n,d)}")
    start_s = pc()
    results = []
    for y in range (np):
        results.append(sphere_volume(n,d))
    vol_s = sum(results)/np
    end_s = pc()
    print(f"Serial execution time: {end_s - start_s:.2f} seconds")  # .2f reduces to 2 decimak
    print(f"Volume approximation (serial): {vol_s}")
    
    start_p1 = pc()
    start_p1 = pc()
    vol_p1 = sphere_volume_parallel1(n, d, np)
    end_p1 = pc()
    print(f"Parallel execution time (for loop): {end_p1 - start_p1:.2f} seconds")
    print(f"Volume approximation (parallel for loop): {vol_p1}")

    end_p2 = pc()
    start_p2 = pc()
    vol_p2 = sphere_volume_parallel2(n, d, np)
    end_p2 = pc()
    print(f"Parallel execution time (data split): {end_p2 - start_p2:.2f} seconds")
    print(f"Volume approximation (parallel data split): {vol_p2}")
    start_p2 = pc()
    
    end_p2 = pc()

if __name__ == '__main__':
	main()