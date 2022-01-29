    # coding=utf-8
"""
This file is your main submission that will be graded against. Only copy-paste
code on the relevant classes included here. Do not add any classes or functions
to this file that are not part of the classes that we want.
"""

import heapq as hq
import os
import pickle
import math


class PriorityQueue(object):
    """
    A queue structure where each element is served in order of priority.

    Elements in the queue are popped based on the priority with higher priority
    elements being served before lower priority elements.  If two elements have
    the same priority, they will be served in the order they were added to the
    queue.

    Traditionally priority queues are implemented with heaps, but there are any
    number of implementation options.

    (Hint: take a look at the module heapq)

    Attributes:
        queue (list): Nodes added to the priority queue.
    """

    def __init__(self):
        """Initialize a new Priority Queue."""

        self.queue = []
        self.entry_count = 0

    def pop(self):
        """
        Pop top priority node from queue.

        Returns:
            The node with the highest priority.
        """

        # TODO: finish this function!
        return hq.heappop(self.queue) # O(logn) Time

    def remove(self, node):
        """
        Remove a node from the queue.

        Hint: You might require this in ucs. However, you may
        choose not to use it or to define your own method.

        Args:
            node (tuple): The node to remove from the queue.
        """

        # searching the item takes O(n), removing and rebalancing takes O(logn)
        # overall O(n)
        for i in range(self.size()):
            if node == (self.queue[i][0],self.queue[i][2]):
                self.queue[i] = self.queue[-1]
                self.queue.pop()
                hq._siftup(self.queue, i)
                return

    def __iter__(self):
        """Queue iterator."""

        return iter(sorted(self.queue))

    def __str__(self):
        """Priority Queue to string."""

        return 'PQ:%s' % self.queue

    def append(self, node):
        """
        Append a node to the queue.

        Args:
            node: Comparable Object to be added to the priority queue.
        """

        # TODO: finish this function!
        self.entry_count += 1
        node = list(node)
        node = tuple([node[0]] + [self.entry_count] + node[1:])
        hq.heappush(self.queue, node) # Average O(1) time, worst O(logn) time

    def __contains__(self, key):
        """
        Containment Check operator for 'in'

        Args:
            key: The key to check for in the queue.

        Returns:
            True if key is found in queue, False otherwise.
        """

        return key in [n[-1] for n in self.queue]

    def __eq__(self, other):
        """
        Compare this Priority Queue with another Priority Queue.

        Args:
            other (PriorityQueue): Priority Queue to compare against.

        Returns:
            True if the two priority queues are equivalent.
        """

        return self.queue == other.queue

    def size(self):
        """
        Get the current size of the queue.

        Returns:
            Integer of number of items in queue.
        """

        return len(self.queue)

    def clear(self):
        """Reset queue to empty (no nodes)."""

        self.queue = []

    def top(self):
        """
        Get the top item in the queue.

        Returns:
            The first item stored in the queue.
        """

        return self.queue[0]

def breadth_first_search(graph, start, goal):
    """
    Warm-up exercise: Implement breadth-first-search.

    See README.md for exercise description.

    Args:
        graph (ExplorableGraph): Undirected graph to search.
        start (str): Key for the start node.
        goal (str): Key for the end node.

    Returns:
        The best path as a list from the start and goal nodes (including both).
    """

    # TODO: finish this function!
    if start == goal:
        return []

    frontier = PriorityQueue()
    explored = set()

    frontier.append((0, [start]))

    while frontier:

        path = frontier.pop()

        s = path[2][-1]
        explored.add(s)

        for a in sorted(graph[s]):
            if (a not in explored) and (not any(a == p[2][-1] for p in frontier)):
                new_path = (path[0]+1,path[2]+[a])
                frontier.append(new_path)
                if a == goal:
                    return new_path[1]
        # import pdb; pdb.set_trace()


def uniform_cost_search(graph, start, goal):
    """
    Warm-up exercise: Implement uniform_cost_search.

    See README.md for exercise description.

    Args:
        graph (ExplorableGraph): Undirected graph to search.
        start (str): Key for the start node.
        goal (str): Key for the end node.

    Returns:
        The best path as a list from the start and goal nodes (including both).
    """

    # TODO: finish this function!
    if start == goal:
        return []

    frontier = PriorityQueue()
    explored = set()

    frontier.append((0, [start]))

    while frontier:

        path = frontier.pop()

        s = path[2][-1]
        if s in explored:
            continue
        else:
            explored.add(s)

        if s == goal:
            return path[2]

        for a in sorted(graph[s]):
            if (a not in explored):
                new_path = (path[0]+graph.get_edge_weight(s,a),path[2]+[a])
                frontier.append(new_path)
        # import pdb; pdb.set_trace()

def null_heuristic(graph, v, goal):
    """
    Null heuristic used as a base line.

    Args:
        graph (ExplorableGraph): Undirected graph to search.
        v (str): Key for the node to calculate from.
        goal (str): Key for the end node to calculate to.

    Returns:
        0
    """

    return 0


def euclidean_dist_heuristic(graph, v, goal):
    """
    Warm-up exercise: Implement the euclidean distance heuristic.

    See README.md for exercise description.

    Args:
        graph (ExplorableGraph): Undirected graph to search.
        v (str): Key for the node to calculate from.
        goal (str): Key for the end node to calculate to.

    Returns:
        Euclidean distance between `v` node and `goal` node
    """

    # TODO: finish this function!
    p_1 = graph.nodes[v]['pos']
    p_2 = graph.nodes[goal]['pos']
    return ((p_2[0]-p_1[0])**2 + (p_2[1]-p_1[1])**2)**0.5


def a_star(graph, start, goal, heuristic=euclidean_dist_heuristic):
    """
    Warm-up exercise: Implement A* algorithm.

    See README.md for exercise description.

    Args:
        graph (ExplorableGraph): Undirected graph to search.
        start (str): Key for the start node.
        goal (str): Key for the end node.
        heuristic: Function to determine distance heuristic.
            Default: euclidean_dist_heuristic.

    Returns:
        The best path as a list from the start and goal nodes (including both).
    """

    # TODO: finish this function!
    if start == goal:
        return []

    frontier = PriorityQueue()
    explored = set()

    frontier.append((0+heuristic(graph, start, goal), [start]))

    while frontier:

        path = frontier.pop()

        s = path[2][-1]
        if s in explored:
            continue
        else:
            explored.add(s)

        if s == goal:
            return path[2]

        for a in sorted(graph[s]):
            if (a not in explored):
                new_path = (path[0] - heuristic(graph, s, goal)
                            + graph.get_edge_weight(s, a)
                            + heuristic(graph, a, goal), path[2]+[a])
                frontier.append(new_path)
        # import pdb; pdb.set_trace()

def bidirectional_ucs(graph, start, goal):
    """
    Exercise 1: Bidirectional Search.

    See README.md for exercise description.

    Args:
        graph (ExplorableGraph): Undirected graph to search.
        start (str): Key for the start node.
        goal (str): Key for the end node.

    Returns:
        The best path as a list from the start and goal nodes (including both).
    """

    # TODO: finish this function!
    def _proceed(bool_forward, frontier_1, explored_1, frontier_2, explored_2, solution):

        path = frontier_1.pop()
        s = path[2][-1]
        if s not in explored_1:
            explored_1[s] = (path[0], path[2])
        elif path[0] < explored_1[s][0]:
            explored_1[s] = (path[0], path[2])
        else:
            return solution

        for a in sorted(graph[s]):
            if (a not in explored_1):
                new_cost = path[0] + graph.get_edge_weight(s, a)
                new_path = (new_cost, path[2]+[a])
                frontier_1.append(new_path)
                if a in explored_2:
                    new_result = new_cost + explored_2[a][0]
                    if new_result < solution[0]:
                        path_1 = new_path[1].copy()
                        path_2 = explored_2[a][1].copy()
                        solution = [new_result, _join_paths(bool_forward, path_1, path_2)]
        return solution

    def _join_paths(bool_forward, path_1, path_2):
        if bool_forward:
            path_2.reverse()
            return path_1 + path_2[1:]
        else:
            path_1.reverse()
            return path_2 + path_1[1:]

    result = [math.inf, []]
    if start == goal:
        return result[1]

    frontier_F = PriorityQueue()
    frontier_B = PriorityQueue()
    explored_F = dict()
    explored_B = dict()

    frontier_F.append((0, [start]))
    frontier_B.append((0, [goal]))

    while frontier_F.queue[0][0] + frontier_B.queue[0][0] < result[0]:
        # import pdb; pdb.set_trace()
        if frontier_F.queue[0][0] <= frontier_B.queue[0][0]:
            result = _proceed(True, frontier_F, explored_F, frontier_B, explored_B, result)
        else:
            result = _proceed(False, frontier_B, explored_B, frontier_F, explored_F, result)

    return result[1]


def bidirectional_a_star(graph, start, goal,
                         heuristic=euclidean_dist_heuristic):
    """
    Exercise 2: Bidirectional A*.

    See README.md for exercise description.

    Args:
        graph (ExplorableGraph): Undirected graph to search.
        start (str): Key for the start node.
        goal (str): Key for the end node.
        heuristic: Function to determine distance heuristic.
            Default: euclidean_dist_heuristic.

    Returns:
        The best path as a list from the start and goal nodes (including both).
    """

    # TODO: finish this function!
    def _proceed(bool_forward, frontier_1, explored_1, frontier_2, explored_2, solution):
        if bool_forward:
            dest = goal
            opp_dest = start
            bool_alt = 0
        else:
            dest = start
            opp_dest = goal
            bool_alt = 1

        path = frontier_1.pop()
        s = path[2][-1]

        if s not in explored_1:
            explored_1[s] = (path[3], path[2])
        elif path[0] < explored_1[s][0]:
            explored_1[s] = (path[3], path[2])
        else:
            return solution, bool_alt

        for a in sorted(graph[s]):
            if a == goal and s == start:
                solution = [graph.get_edge_weight(s, a), [s, a]]

            if (a not in explored_1):
                old_g = path[3]
                g = old_g + graph.get_edge_weight(s, a)

                if bool_forward:
                    h = 0.5 * (heuristic(graph, a, goal) - heuristic(graph, a, start) + heuristic(graph, goal, start))
                else:
                    h = 0.5 * (heuristic(graph, a, start) - heuristic(graph, a, goal) + heuristic(graph, start, goal))

                new_f = g + h
                new_path = (new_f, path[2]+[a], g)
                frontier_1.append(new_path)
                if a in explored_2:
                    new_result = g + explored_2[a][0]
                    if new_result < solution[0]:
                        path_1 = new_path[1].copy()
                        path_2 = explored_2[a][1].copy()
                        solution = [new_result, _join_paths(bool_forward, path_1, path_2)]
        return solution, bool_alt

    def _join_paths(bool_forward, path_1, path_2):
        if bool_forward:
            path_2.reverse()
            return path_1 + path_2[1:]
        else:
            path_1.reverse()
            return path_2 + path_1[1:]

    result = [math.inf, []]
    if start == goal:
        return result[1]

    frontier_F = PriorityQueue()
    frontier_B = PriorityQueue()
    explored_F = dict()
    explored_B = dict()

    frontier_F.append((0.5 * (heuristic(graph, start, goal) + heuristic(graph, goal, start)), [start], 0))
    frontier_B.append((0.5 * (heuristic(graph, goal, start) + heuristic(graph, start, goal)), [goal], 0))

    bool_alt = 1
    while frontier_F.queue[0][0] + frontier_B.queue[0][0] < result[0] + heuristic(graph, goal, start):
        # import pdb; pdb.set_trace()
        if bool_alt:
            result, bool_alt = _proceed(True, frontier_F, explored_F, frontier_B, explored_B, result)
        else:
            result, bool_alt = _proceed(False, frontier_B, explored_B, frontier_F, explored_F, result)

    return result[1]

def tridirectional_search(graph, goals):
    """
    Exercise 3: Tridirectional UCS Search

    See README.MD for exercise description.

    Args:
        graph (ExplorableGraph): Undirected graph to search.
        goals (list): Key values for the 3 goals

    Returns:
        The best path as a list from one of the goal nodes (including both of
        the other goal nodes).
    """

    # internal helper functions
    def _proceed(idx, frontiers, explored, solution):
        if check_optimal(idx, frontiers, solution):
            frontiers[idx].pop()
            return solution

        path = frontiers[idx].pop()
        s = path[2][-1]
        if s not in explored[idx]:
            explored[idx][s] = (path[0], path[2])
        elif path[0] < explored[idx][s][0]:
            explored[idx][s] = (path[0], path[2])
        else:
            return solution

        for a in sorted(graph[s]):
            pool = [0, 1, 2]
            pool.remove(idx)

            if (a not in explored[idx]):
                new_cost = path[0] + graph.get_edge_weight(s, a)
                new_path = (new_cost, path[2]+[a])
                frontiers[idx].append(new_path)
                for j in pool:
                    if a in explored[j] and new_cost < solution[idx][j][0]:
                        new_result = new_cost + explored[j][a][0]
                        path_1 = new_path[1].copy()
                        path_2 = explored[j][a][1].copy()
                        combined_path = _join_path(path_1, path_2)
                        reverse_path = combined_path.copy()
                        combined_path.reverse()
                        if new_result < solution[idx][j][0]:
                            solution[idx][j] = [new_result, combined_path]
                            solution[j][idx] = [new_result, reverse_path]

        return solution

    def _join_path(path_1, path_2):
        if path_1 == path_2[::-1]:
            return path_1
        else:
            path_2.reverse()
            return path_1 + path_2[1:]

    def _calc_path(results):
        list_paths = []
        for i in range(3):
            for key, result in results[i].items():
                if (result[0] != math.inf) and not any((result[1][::-1] == _[1] or result[1] == _[1]) for _ in list_paths):
                    list_paths.append(result)

        list_paths.sort(key = lambda k:k[0])
        if len(list_paths) > 2:
            list_paths.pop()
        elif len(list_paths) < 2:
            return list_paths[0][1]

        list_paths = [list_paths[0][1], list_paths[1][1]]

        if list_paths[0][0] == list_paths[1][0]:
            list_paths[0].reverse()
        elif list_paths[0][-1] == list_paths[1][-1]:
            list_paths[1].reverse()
        elif list_paths[0][0] == list_paths[1][-1]:
            list_paths[0].reverse()
            list_paths[1].reverse()
        return list_paths[0] + list_paths[1][1:]

    def terminate(frontiers, solution):
        min_0, min_1, min_2 = [frontiers[_].queue[0][0] for _ in range(3)]
        b_0 = ((min_0 + min_1) >= solution[0][1][0])
        b_1 = ((min_0 + min_2) >= solution[0][2][0])
        b_2 = ((min_1 + min_2) >= solution[1][2][0])
        return b_0 and b_1 and b_2

    def check_optimal(idx, frontiers, solution):
        pool = [0, 1, 2]
        pool.remove(idx)
        min_idx = frontiers[idx].queue[0][0]
        for j in pool:
            min_goal = frontiers[j].queue[0][0]
            if min_idx + min_goal < solution[idx][j][0]:
                return False
        return True

    # if three goals are identical, return []
    result = [math.inf, []]
    if goals[1] == goals[2] and goals[1] == goals[3]:
        return

    # define and initiate frontiers, explored, and result for each goal
    if len(goals) == 3:
        frontiers = {i:PriorityQueue() for i in range(3)}
        explored = {i:dict() for i in range(3)}
        results = {0:dict(), 1:dict(), 2:dict()}
        for i in range(3):
            k = [0, 1, 2]
            k.remove(i)
            for j in k:
                temp = {j:[math.inf, []]}
                results[i].update(temp.copy())
        for i in range(3):
            frontiers[i].append((0, [goals[i]]))
            frontiers[i].append((math.inf, []))
        mu = math.inf

    # terminate when stopping condition met - two edges have been found
        # expand three goals by minimum of three frontiers
        while not terminate(frontiers, results):
            # import pdb; pdb.set_trace()
            idx = min(frontiers.items(), key = lambda k:k[1].queue[0][0])[0]
            result = _proceed(idx, frontiers, explored, results)
        # import pdb; pdb.set_trace()
        tri_path = _calc_path(results)
    return tri_path

def tridirectional_upgraded(graph, goals, heuristic=euclidean_dist_heuristic, landmarks=None):
    """
    Exercise 4: Upgraded Tridirectional Search

    See README.MD for exercise description.

    Args:
        graph (ExplorableGraph): Undirected graph to search.
        goals (list): Key values for the 3 goals
        heuristic: Function to determine distance heuristic.
            Default: euclidean_dist_heuristic.
        landmarks: Iterable containing landmarks pre-computed in compute_landmarks()
            Default: None

    Returns:
        The best path as a list from one of the goal nodes (including both of
        the other goal nodes).
    """

    # internal helper functions
    def _tri_proceed(idx, frontiers, explored, solution):
        bool_terminate, connected = False, []
        path = frontiers[idx].pop()
        s = path[2][-1]
        if s not in explored[idx]:
            explored[idx][s] = (path[3], path[2])
        elif path[3] < explored[idx][s][0]:
            explored[idx][s] = (path[3], path[2])
        else:
            return solution

        for a in sorted(graph[s]):
            pool = [0, 1, 2]
            pool.remove(idx)

            if (a not in explored[idx]):
                g = path[3] + graph.get_edge_weight(s, a)
                h = []
                for j in pool:
                    h.append(0.5 * (heuristic(graph, a, goals[j]) - heuristic(graph, a, goals[idx])))
                f = g + min(h)
                new_path = (f, path[2]+[a], g)
                frontiers[idx].append(new_path)
                for j in pool:
                    if a in explored[j] and f < solution[idx][j][0]:
                        new_result = g + explored[j][a][0]
                        path_1 = new_path[1].copy()
                        path_2 = explored[j][a][1].copy()
                        combined_path = _join_path(path_1, path_2)
                        reverse_path = combined_path.copy()
                        combined_path.reverse()
                        if new_result < solution[idx][j][0]:
                            solution[idx][j] = [new_result, combined_path]
                            solution[j][idx] = [new_result, reverse_path]
                            bool_terminate = True
                            connected.append([idx, j])
        return solution, bool_terminate, connected

    def _bi_proceed(goal, frontier_1, frontier_2, explored_1, explored_2, solution):
        path = frontier_1.pop()
        s = path[2][-1]
        idx = goals.index(s)
        if s not in explored_1 or path[3] < explored_1[s][0]:
            explored_1[s] = (path[3], path[2])
        else:
            return solution

        for a in sorted(graph[s]):
            if (a not in explored_1):
                g = path[3] + graph.get_edge_weight(s, a)
                if len(goal) == 2:
                    h = []
                    for j in goal:
                        h.append(0.5 * (heuristic(graph, a, goals[j]) - heuristic(graph, a, goals[idx])))
                    f = g + min(h)
                    if any((a == frontier[2][-1] and f > frontier[0]) for frontier in frontier_1):
                        return solution
                else:
                    h = 0.5 * (heuristic(graph, a, goals[goal]) - heuristic(graph, a, goals[goal]))
                    f = g + h
                new_path = (f, path[2]+[a], g)
                frontier_1.append(new_path)
                if a in explored_2:
                    new_result = g + explored_2[a][0]
                    path_1 = new_path[1].copy()
                    path_2 = explored_2[a][1].copy()
                    combined_path = _join_path(path_1, path_2)
                    reverse_path = combined_path.copy()
                    combined_path.reverse()
                    if new_result < solution[idx][goal][0]:
                        solution[idx][goal] = [new_result, combined_path]
                        solution[goal][idx] = [new_result, reverse_path]
        return solution

    def _join_path(path_1, path_2):
        if path_1 == path_2[::-1]:
            return path_1
        else:
            path_2.reverse()
            return path_1 + path_2[1:]

    def _calc_path(results):
        list_paths = []
        for i in range(3):
            for key, result in results[i].items():
                if (result[0] != math.inf) and not any((result[1][::-1] == _[1] or result[1] == _[1]) for _ in list_paths):
                    list_paths.append(result)

        list_paths.sort(key = lambda k:k[0])
        if len(list_paths) > 2:
            list_paths.pop()
        elif len(list_paths) < 2:
            return list_paths[0][1]

        list_paths = [list_paths[0][1], list_paths[1][1]]

        if list_paths[0][0] == list_paths[1][0]:
            list_paths[0].reverse()
        elif list_paths[0][-1] == list_paths[1][-1]:
            list_paths[1].reverse()
        elif list_paths[0][0] == list_paths[1][-1]:
            list_paths[0].reverse()
            list_paths[1].reverse()
        return list_paths[0] + list_paths[1][1:]

    def _bi_terminate(frontier_1, frontier_2, solution, connected, unconnected):
        min_F = frontier_1.queue[0][0]
        min_B = frontier_2.queue[0][0]
        for j in connected:
        return bool_pool[0] and bool_pool[1]

    def _convert_frontiers(connected, unconnected, frontiers):
        frontier_F = PriorityQueue()
        frontier_B = PriorityQueue()
        for j in connected:
            while frontiers[j].size() > 1:
                node = frontiers[j].pop()
                v = node[2][-1]
                new_cost = node[3] + 0.5 * (heuristic(graph, v, goals[unconnected]) - heuristic(graph, v, goals[j]))
                frontier_F.append((new_cost, node[2], node[3]))
            frontier_F.append((math.inf, [], math.inf))
        while frontiers[unconnected].size() > 0:
            node = frontiers[unconnected].pop()
            frontier_B.append((node[0], node[2],node[3]))
        return frontier_F, frontier_B

    def _convert_explored(connected, unconnected, explored):
        explored_1, explored_2 = dict(), dict()
        explored_1 = explored[connected[0]].copy()
        explored[connected[0]].clear()
        for key, value in explored[connected[1]]:
            if key not in explored_1:
                explored_1[key] = value
            elif value[0] < explored_1[key][0]:
                explored_1[key] = value
        explored[connected[1]].clear()
        explored_2 = explored[unconnected]
        explored[unconnected].clear()
        return explored_1, explored_2

    # if three goals are identical, return []
    result = [math.inf, []]
    if goals[1] == goals[2] and goals[1] == goals[3]:
        return

    # define and initiate frontiers, explored, and result for each goal
    if len(goals) == 3:
        frontiers = {i:PriorityQueue() for i in range(3)}
        explored = {i:dict() for i in range(3)}
        results = {0:dict(), 1:dict(), 2:dict()}
        for i in range(3):
            k = [0, 1, 2]
            k.remove(i)
            for j in k:
                temp = {j:[math.inf, []]}
                results[i].update(temp.copy())
        for i in range(3):
            pool = [0, 1, 2]
            pool.remove(i)
            h = []
            for j in pool:
                h.append(0.5 * (heuristic(graph, goals[i], goals[j])))
            frontiers[i].append((min(h), [goals[i]], 0))
            frontiers[i].append((math.inf, [], math.inf))
        tri_terminate = False

    # terminate when stopping condition met - two edges have been found
        # expand three goals by minimum of three frontiers
        while not tri_terminate:
            # import pdb; pdb.set_trace()
            idx = min(frontiers.items(), key = lambda k:k[1].queue[0][0])[0]
            results, tri_terminate, connected = _tri_proceed(idx, frontiers, explored, results)
            # import pdb; pdb.set_trace()

        unconnected = [element for element in [0, 1, 2] if element not in connected]
        frontier_F, frontier_B = _convert_frontiers(connected, unconnected, frontiers)
        explored_F, explored_B = _convert_explored(connected, unconnected, explored)

        while not _bi_terminate(frontiers, results, unconnected):
            # import pdb; pdb.set_trace()
            if frontier_F.queue[0][0] < frontier_B.queue[0][0]:
                results = _bi_proceed(unconnected, frontier_F, frontier_B, explored_F, explored_B, solution)
            else:
                results = _bi_proceed(connected, frontier_F, frontier_B, explored_F, explored_B, solution)
            # import pdb; pdb.set_trace()

        tri_path = _calc_path(results)
    return tri_path

def return_your_name():
    """Return your name from this function"""
    # TODO: finish this function
    return 'Zi Sang'


def compute_landmarks(graph):
    """
    Feel free to implement this method for computing landmarks. We will call
    tridirectional_upgraded() with the object returned from this function.

    Args:
        graph (ExplorableGraph): Undirected graph to search.

    Returns:
    List with not more than 4 computed landmarks.
    """
    return None


def custom_heuristic(graph, v, goal):
    """
       Feel free to use this method to try and work with different heuristics and come up with a better search algorithm.
       Args:
           graph (ExplorableGraph): Undirected graph to search.
           v (str): Key for the node to calculate from.
           goal (str): Key for the end node to calculate to.
       Returns:
           Custom heuristic distance between `v` node and `goal` node
       """
    pass


# Extra Credit: Your best search method for the race
def custom_search(graph, start, goal, data=None):
    """
    Race!: Implement your best search algorithm here to compete against the
    other student agents.

    If you implement this function and submit your code to Gradescope, you'll be
    registered for the Race!

    See README.md for exercise description.

    Args:
        graph (ExplorableGraph): Undirected graph to search.
        start (str): Key for the start node.
        goal (str): Key for the end node.
        data :  Data used in the custom search.
            Will be passed your data from load_data(graph).
            Default: None.

    Returns:
        The best path as a list from the start and goal nodes (including both).
    """

    # TODO: finish this function!
    raise NotImplementedError


def load_data(graph, time_left):
    """
    Feel free to implement this method. We'll call it only once
    at the beginning of the Race, and we'll pass the output to your custom_search function.
    graph: a networkx graph
    time_left: function you can call to keep track of your remaining time.
        usage: time_left() returns the time left in milliseconds.
        the max time will be 10 minutes.

    * To get a list of nodes, use graph.nodes()
    * To get node neighbors, use graph.neighbors(node)
    * To get edge weight, use graph.get_edge_weight(node1, node2)
    """

    # nodes = graph.nodes()
    return None


def haversine_dist_heuristic(graph, v, goal):
    """
    Note: This provided heuristic is for the Atlanta race.

    Args:
        graph (ExplorableGraph): Undirected graph to search.
        v (str): Key for the node to calculate from.
        goal (str): Key for the end node to calculate to.

    Returns:
        Haversine distance between `v` node and `goal` node
    """

    #Load latitude and longitude coordinates in radians:
    vLatLong = (math.radians(graph.nodes[v]["pos"][0]), math.radians(graph.nodes[v]["pos"][1]))
    goalLatLong = (math.radians(graph.nodes[goal]["pos"][0]), math.radians(graph.nodes[goal]["pos"][1]))

    #Now we want to execute portions of the formula:
    constOutFront = 2*6371 #Radius of Earth is 6,371 kilometers
    term1InSqrt = (math.sin((goalLatLong[0]-vLatLong[0])/2))**2 #First term inside sqrt
    term2InSqrt = math.cos(vLatLong[0])*math.cos(goalLatLong[0])*((math.sin((goalLatLong[1]-vLatLong[1])/2))**2) #Second term
    return constOutFront*math.asin(math.sqrt(term1InSqrt+term2InSqrt)) #Straight application of formula
