
"""
Solutions to module 4
Review date:
"""

student = "Marta Carvalho"
reviewer = ""


import random as r
import matplotlib.pyplot as plt 
import math 
import numpy as np 


def approximate_pi(n):
    
    x = np.random.uniform(-1,1,n)
    y = np.random.uniform(-1,1,n)
    nc = 0
    nc_x = []
    nc_y = []
    ns_x = []
    ns_y = []
    
    for i in range(n):
        if (x[i]**2 + y[i]**2)**0.5 == 1 or (x[i]**2 + y[i]**2)**0.5 < 1:
            nc+=1
            nc_x.append(x[i])
            nc_y.append(y[i])
        else:
            ns_x.append(x[i])
            ns_y.append(y[i])
            
    pi = 4*nc / n
    print('Number of points inside the circle: ', nc)
    print('Approximation of pi for n=', n,': ', pi)
    print('Real pi value: ', math.pi)
 
    # Plot
    plt.figure(figsize=(8, 8))
    
    plt.scatter(nc_x, nc_y, color='red', label='Inside Circle')
    plt.scatter(ns_x, ns_y, color='blue', label='Outside Circle')

    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()
    
    return pi
    
def main():
    dots = [1000, 10000, 100000]
    for n in dots:
        approximate_pi(n)

if __name__ == '__main__':
	main()
