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
#    imported for you.
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
        return iter(sorted(self.queue))

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


# Warm-up 2: BFS
# ----------
# 5 pts
#
#
# To get you started with handling graphs in networkx, implement and test
# breadth-first search over the test network.
#
# You'll do complete this by writing the "breadth_first_search" method. This
# returns a path of nodes from a given start node to a given end node, as a
# list.
#
# For this part, it is optional to use the PriorityQueue as your frontier. You
# will require it from the next question onwards. You can use it here too if
# you want to be consistent.
#
# Notes:
# 1. You need to include start and goal in the path.
# 2. If your start and goal are the same then just return [].
#
# Both of the above are just to keep your results consistent with our test
# cases.
#
# You can access all the neighbors of a given node by calling graph[node], or
# graph.neighbors(node) ONLY. To measure your search performance, a modified
# version of the networkx Graph class is provided. It keeps track of which
# nodes you have accessed in this way (this is referred to as the set of
# 'Explored' nodes). To retrieve the set of nodes you've explored in this way,
# check the 'graph.explored_nodes' property. If you wish to perform multiple
# searches on the same graph instance, call 'graph.reset_search()' to clear out
# the current set of 'Explored' nodes. Note however, that you will not have
# access to these modifications on the test server. Also, there is no need to
# reset the graph while submitting to the test server.
def breadth_first_search(graph, start, goal):
    """
    Run a breadth-first search from start
    to goal and return the path.
    """
    # TODO: finish this function!
    raise NotImplementedError


# Warmup Examples
# ----------
#
# Some examples of correct warmup searches can be found [here](https://docs.google.com/document/d/18Bl7awruAabUXAhMy-T88hWKTteueEb7hk6gA32GulQ/pub).


# Warmup 3: Uniform-cost search
# ----------------------------
# 10 points
#
# Implement uniform-cost search, using PriorityQueue as your frontier. From now
# on, PriorityQueue should be your default frontier.
#
# uniform_cost_search() should return the same arguments as breadth-first
# search: the path to the goal node (as a list of nodes).
#
#
# Notes:
# 1. You do need to include start and goal in the path.
# 2. If your start and goal are the same then just return []
# 3. We will provide some margin of error in grading the size of your
#    'Explored' set, but it should be close to the results provided by our
#    reference implementation.
#
# The above are just to keep your results consistent with our test cases.
def uniform_cost_search(graph, start, goal):
    """
    Run uniform-cost search from start
    to goal and return the path.
    """
    # TODO: finish this function
    raise NotImplementedError


# Warmup 4: A* search
# ------------------
# 10 points
# Implement A* search using Euclidean distance as your heuristic. You'll need
# to implement heuristic_euclid() then pass that function to a_star() as the
# heuristic parameter. We provide null_heuristic() as a baseline heuristic to
# test against when calling a_star tests.
#
# Hint: you can find a node's position by calling:
#
#      graph.node[n]['pos']      - Romania map
#      graph.node[n]['position'] - Atlanta map
#
# Tip: use graph.node[n].get('position') or graph.node[n].get('pos') to check
# if the key is available.
#
# Notes:
# 1. You do need to include start and goal in the path.
# 2. If your start and goal are the same then just return []
# 3. We will provide some margin of error in grading the size of your
#    'Explored' set, but it should be close to the results provided by our
#    reference implementation.
#
# The above are just to keep your results consistent with our test cases.
def null_heuristic(graph, v, goal):
    """Return 0 for all nodes."""
    return 0


def euclidean_dist_heuristic(graph, v, goal):
    """
    Return the Euclidean distance from
    node v to the goal.
    """
    # TODO: finish this function
    raise NotImplementedError


def a_star(graph, start, goal, heuristic=euclidean_dist_heuristic):
    """
    Run A* search from the start to
    goal using the specified heuristic
    function, and return the final path.
    """
    # TODO: finish this function
    raise NotImplementedError


# Exercises
# -------
#
#
# The following exercises will require you to implement several kinds of
# bidirectional and tri-directional searches. For these exercises, we recommend
# you take a look at the [resources](https://github.gatech.edu/omscs6601/assignment_2/tree/master/resources)
# folder in the assignment repo and the notes linked in the assignment repo's
# [README](https://github.gatech.edu/omscs6601/assignment_2/blob/master/README.md).
#
# The benefits of these algorithms over uninformed or unidirectional search are
# more clearly seen on larger graphs. As such, during grading, we will evaluate
# your performance on the map of Atlanta [OpenStreetMap](http://wiki.openstreetmap.org/)
# included in this assignment. If you want to run tests using this data (rather
# than just testing on the server), you'll need to load the data from the file.
# If you're testing locally, be advised, not all nodes are connected.

# Exercise 1: Bidirectional uniform-cost search
# -------
# 15 points
#
# Implement bidirectional uniform-cost search. Remember that this requires
# starting your search at both the start and end states.
#
# bidirectional_ucs() should return the path from the start node to the goal
# node (as a list of nodes).
#
# Notes:
#     1) You do need to include start and goal in the path.
#     2) If your start and goal are the same then just return []
#     3) We will provide some margin of error in grading the size of your
#        'Explored' set, but it should be close to the results provided by our
#        reference implementation.
#
#
# All of the above are just to keep your results consistent with our test cases
def bidirectional_ucs(graph, start, goal):
    """
    Run bidirectional uniform-cost search
    between start and goal
    """
    # TODO: finish this function
    raise NotImplementedError


# Exercise 2: Bidirectional A* search
# -------
# 20 points
#
# Implement bidirectional A* search. Remember that you need to calculate a
# heuristic for both the start-to-goal search and the goal-to-start search.
#
# To test this function, as well as using the provided tests, you can compare
# the path computed by bidirectional A star to bidirectional ucs search above.
#
# bidirectional_a_star should return the path from the start node to the goal
# node, as a list of nodes.
#
# Notes:
#     1) You do need to include start and goal in the path.
#     2) If your start and goal are the same then just return []
#     3) We will provide some margin of error in grading the size of your
#        'Explored' set, but it should be close to the results provided by our
#        reference implementation.
def bidirectional_a_star(graph, start, goal,
                         heuristic=euclidean_dist_heuristic):
    """
    Run bidirectional A* search between
    start and goal.
    """
    # TODO: finish this function
    raise NotImplementedError


# Race!
# ---
# Here's your chance to show us your best stuff. This part is mandatory if you
# want to compete in the race for extra credit. Implement custom_search() using
# whatever strategy you like. Your search should be tri-directional and it'll
# be tested on the Atlanta map only.
def custom_search(graph, goals):
    """
    Run your best tri-directional search between
    goals, and return the path.
    """
    raise NotImplementedError


# Extra Credit: Your best search method for the race
# Loads data from data.pickle and return the data object that is passed to the
# custom_search method. Will be called only once. Feel free to modify.
def load_data():
    path = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                        "data.pickle")
    data = pickle.load(open(path, 'rb'))
    return data
