# -*- coding: utf-8 -*-
"""
Spyder Editor

Problem 3 from Homework 1, PTYS595B Fall 2016
Alexander Prescott
"""

import numpy as np
import pylab as plt


pts = np.random.rand(1000,2)*2-1

dist = np.power(pts[:,0],2)+np.power(pts[:,1],2)
dist = np.sqrt(dist)

in_pts = pts[np.nonzero(dist<1)[0],:]

plt.figure(1)
plt.scatter(in_pts[:,0],in_pts[:,1])
plt.gca().set_aspect(aspect='equal',adjustable='datalim')

tran1 = np.array([[-1,2],[2,-1]])
tran2 = np.array([[2,3],[3,2]])
tran3 = np.array([[3,1],[1,3]])
tran4 = np.array([[9,10],[10,9]])

tran1_dots=np.dot(tran1,in_pts.T).T
tran2_dots=np.dot(tran2,in_pts.T).T
tran3_dots=np.dot(tran3,in_pts.T).T
tran4_dots=np.dot(tran4,in_pts.T).T

plt.figure(2)
plt.scatter(tran1_dots[:,0],tran1_dots[:,1])
plt.gca().set_aspect('equal',adjustable='box')

plt.figure(3)
plt.scatter(tran2_dots[:,0],tran2_dots[:,1])
plt.gca().set_aspect('equal',adjustable='box')

plt.figure(4)
plt.scatter(tran3_dots[:,0],tran3_dots[:,1])
plt.gca().set_aspect('equal',adjustable='box')

plt.figure(5)
plt.scatter(tran4_dots[:,0],tran4_dots[:,1])
plt.gca().set_aspect('equal',adjustable='box')

print np.linalg.eig(tran1)
print np.linalg.eig(tran2)
print np.linalg.eig(tran3)
print np.linalg.eig(tran4)