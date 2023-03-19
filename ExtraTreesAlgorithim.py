from sklearn import datasets
import random
import math
import numpy as np
iris = datasets.load_iris()
S= iris.data[:, :2]
M=100 #100 trees

class Node:
     def __init__(self,data):
          self.data = data
          self.left = None
          self.right = None

     def __repr__(self):
          return repr(self.data)

     def add_left(self,node):
         self.left = node

     def add_right(self,node):
         self.right = node

#project code
def Build_an_extra_tree_ensemble(s):
  T = [0 for element in range(M)]
  for i in range(1,M):
    T[i] = Build_an_extra_tree(s)
  return T

#recursive function
def Build_an_extra_tree(s):
  #base case 1
  if abs(s) < nMin:
    return 0
  #base case 2
  
  #base case 3

  #recursive case
  