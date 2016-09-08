# This file is your main submission that will be graded against. Only copy-paste
# code on the relevant classes included here from the IPython notebook. Do not
# add any classes or functions to this file that are not part of the classes
# that we want.
from __future__ import division
import math
from osm2networkx import *
import random
import pickle
import sys
# import matplotlib.pyplot as plt

# Implement a heapq backed priority queue (accompanying the relevant question)
import heapq

class PriorityQueue():
    
    # HINT look up the module heapq.

    def __init__(self):
        self.queue = []
        self.current = 0        

    def next(self):
        if self.current >=len(self.queue):
            self.current
            raise StopIteration
    
        out = self.queue[self.current]
        self.current += 1

        return out

    def pop(self):
        raise NotImplementedError

    def remove(self, other):
        raise NotImplementedError
    
    def __iter__(self):
        return self

    def __str__(self):
        return 'PQ:[%s]'%(', '.join([str(i) for i in self.queue]))

    def append(self, node):
        raise NotImplementedError

    def __contains__(self, key):
        self.current = 0
        return key in [n for v,n in self.queue]

    def __eq__(self, other):
        self.current = 0
        return self == other

    __next__ = next

#Warmup exercise: Implement breadth-first-search
def breadth_first_search(graph, start, goal):
    raise NotImplementedError

#Warmup exercise: Implement uniform_cost_search
def uniform_cost_search(graph, start, goal):
    raise NotImplementedError

# Warmup exercise: Implement A*
def null_heuristic(graph, u, v, goal ):
    return 0

# Warmup exercise: Implement the euclidean distance heuristic
def euclidean_dist_heuristic(graph, u, v, goal):
    raise NotImplementedError

# Warmup exercise: Implement A* algorithm
def a_star(graph, start, goal, heuristic):
    raise NotImplementedError

# Exercise 1: Bidirectional Search
def bidirectional_ucs(graph, start, goal, heuristic=null_heuristic):
    raise NotImplementedError

# Exercise 2: Bidirectional A*
def bidirectional_a_star(graph, start, goal, heuristic=null_heuristic):
    raise NotImplementedError

# Exercise 3: Tridirectional Search
def tridirectional_search(graph, goals):
    raise NotImplementedError

# Exercise 4: Present an improvement on tridirectional search in terms of nodes explored
def tridirectional_upgraded(graph, goals, heuristic):
    raise NotImplemented

