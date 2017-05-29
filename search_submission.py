# coding=utf-8
"""
This file is your main submission that will be graded against. Only copy-paste
code on the relevant classes included here from the IPython notebook. Do not
add any classes or functions to this file that are not part of the classes
that we want.
"""

from __future__ import division

import heapq
import pickle

import os


# Warmups
# ------
# We'll start by implementing some simpler optimization and search algorithms
# before the real exercises.

# Warmup 1: Priority queue
# ----------------------
# 5 points
#
# In all searches that involve calculating path cost or heuristic (e.g.
# uniform-cost), we have to order our search frontier. It turns out the way
# that we do this can impact our overall search runtime.
#
# To show this, you'll implement a [priority queue](https://en.wikipedia.org/wiki/Priority_queue)
# and demonstrate its performance benefits. For large graphs, sorting all input
# to a priority queue is impractical. As such, the data structure you implement
# should have an amortized O(1) insertion and O(lg n) removal time. It should
# do better than the naive implementation in our tests (InsertionSortQueue),
# which sorts the entire list after every insertion.
#
# Hints:
# 1. The [heapq](https://docs.python.org/2/library/heapq.html) module has been
# imported for you.
# 2. Each edge has an associated weight.
# Implement a heapq backed priority queue (accompanying the relevant question)
class PriorityQueue(object):
    """
    Implementation of a priority queue
    to store nodes during search.
    """

    # TODO: finish this class
    # HINT look up/use the module heapq.

    def __init__(self):
        self.queue = []

    def pop(self):
        # TODO: finish this
        raise NotImplementedError

    # TODO: This is a hint, you might require this in ucs,
    # however, if you choose not to use it, you are free to
    # define your own method and not use it.
    def remove(self, node_id):
        raise NotImplementedError

    def __iter__(self):
        return iter(self.queue)

    def __str__(self):
        return 'PQ:%s' % self.queue

    def append(self, node):
        # TODO: finish this
        raise NotImplementedError

    def __contains__(self, key):
        return key in [n for _, n in self.queue]

    def __eq__(self, other):
        return self == other

    def size(self):
        return len(self.queue)

    def clear(self):
        self.queue = []

    def top(self):
        return self.queue[0]

    __next__ = next

#Warmup exercise: Implement breadth-first-search
def breadth_first_search(graph, start, goal):
    raise NotImplementedError

#Warmup exercise: Implement uniform_cost_search
def uniform_cost_search(graph, start, goal):
    raise NotImplementedError

# Warmup exercise: Implement A*
def null_heuristic(graph, v, goal ):
    return 0

# Warmup exercise: Implement the euclidean distance heuristic
def euclidean_dist_heuristic(graph, v, goal):
    raise NotImplementedError

# Warmup exercise: Implement A* algorithm
def a_star(graph, start, goal, heuristic=euclidean_dist_heuristic):
    raise NotImplementedError

# Exercise 1: Bidirectional Search
def bidirectional_ucs(graph, start, goal):
    raise NotImplementedError

# Exercise 2: Bidirectional A*
def bidirectional_a_star(graph, start, goal, heuristic=euclidean_dist_heuristic):
    raise NotImplementedError

# Exercise 3: Tridirectional UCS Search
def tridirectional_search(graph, goals):
    raise NotImplementedError

# Exercise 4: Present an improvement on tridirectional search in terms of nodes explored
def tridirectional_upgraded(graph, goals, heuristic=euclidean_dist_heuristic):
    raise NotImplementedError

# Extra Credit: Your best search method for the race
# Loads data from data.pickle and return the data object that is passed to the custom_search method. Will be called only once. Feel free to modify.
def load_data():
    data = pickle.load(open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "data.pickle"), 'rb'))
    return data

def custom_search(graph, goals, data=None):
    raise NotImplementedError
