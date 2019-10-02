# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 12:28:15 2019

@author: timsc
"""

import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("iris.csv", delimiter=",")


'''
print("Numer of flowers of type 1")
print(np.count_nonzero(data[:,4] == 1))

print("Numer of flowers of type 2")
print(np.count_nonzero(data[:,4] == 2))

print("Numer of flowers of type 0")
print(np.count_nonzero(data[:,4] == 0))
'''

X = data[:,:4].T
T = data[:,4].T

x = X[0,:]
y = X[1,:]

plt.scatter(x, y, c=T, cmap=plt.cm.prism)

def neuron(X):
    W = [-0.3, 1]
    no_Features = 2 # needs to match the size of W !
    A = 1
    
    N=X.shape[1]
    net = np.zeros(X.shape[1])


    for n in range(0,N):
        for j in range(0,no_Features):
            # add the sum of both the features (see no_Features) to the n'th position
            # in net
            
            net[n]+= X[j,n]*W[j]
            # print(X[j,n], "--", W[j])
            

    return net > A

lala = neuron(X)
