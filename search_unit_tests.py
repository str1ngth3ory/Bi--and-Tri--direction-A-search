import unittest
import pickle
import random
import networkx

from search_submission import (breadth_first_search, uniform_cost_search,
                               null_heuristic, euclidean_dist_heuristic,
                               a_star, bidirectional_ucs, bidirectional_a_star)


class SearchUnitTests(unittest.TestCase):
    """Error Diagnostic code courtesy one of our former students -  Mac Chan

        The following unit tests will check for all pairs on romania and random
        points on atlanta.
        Comment out any tests that you haven't implemented yet.

        If you failed on bonnie because of non-optimal path, make sure you pass
        all the local tests.
        Change ntest=-1 if you failed the path test on bonnie, it will run tests
        on atlanta until it finds a set of points that fail.

        If you failed on bonnie because of your explored set is too large, there
        is no easy way to test without a reference implementation.
        But you can read the pdf slides for the optimized terminal condition.

        To run,
        nosetests --nocapture -v search_unit_tests.py:SearchUnitTests
        nosetests --nocapture -v
            search_unit_tests.py:SearchUnitTests.test_tucs_romania
    """

    margin_of_error = 1.0e-6

    def setUp(self):
        self.romania = pickle.load(open('romania_graph.pickle', 'rb'))
        self.romania.reset_search()
        self.atlanta = pickle.load(open('atlanta_osm.pickle', 'rb'))
        self.atlanta.reset_search()

    def reference_path(self, g, src, dst, weight='weight'):
        g.reset_search()
        p = networkx.shortest_path(g, src, dst, weight=weight)
        c = self.sum_weight(g, p)
        return c, p

    def reference_bfs_path(self, g, src, dst):
        return self.reference_path(g, src, dst, weight=None)

    def sum_weight(self, g, path):
        pairs = zip(path, path[1:])
        return sum([g.get_edge_data(a, b)['weight'] for a, b in pairs])

    def romania_test(self, ref_method, method, assert_explored=False, **kwargs):
        keys = self.romania.node.keys()
        pairs = zip(keys, keys[1:])
        for src, dst in pairs:
            self.romania.reset_search()
            path = method(self.romania, src, dst, **kwargs)
            explored = len(self.romania.get_explored_nodes())
            ref_len, ref_path = ref_method(self.romania, src, dst)
            ref_explored = len(self.romania.get_explored_nodes())
            if path != ref_path:
                print src, dst
            assert path == ref_path
            if assert_explored:
                assert explored <= ref_explored

    def atlanta_bi_test(self, method, n_test=10, assert_explored=False,
                        **kwargs):
        keys = list(networkx.connected_components(self.atlanta).next())
        random.shuffle(keys)
        for src, dst in zip(keys, keys[1:])[::2]:
            self.atlanta.reset_search()
            path = method(self.atlanta, src, dst, **kwargs)
            explored = len(self.atlanta.get_explored_nodes())
            path_len = self.sum_weight(self.atlanta, path)
            ref_len, ref_path = self.reference_path(self.atlanta, src, dst)
            ref_explored = len(self.atlanta.get_explored_nodes())
            if abs(path_len - ref_len) > self.margin_of_error:
                print src, dst
            assert abs(path_len - ref_len) <= self.margin_of_error
            if assert_explored:
                assert explored <= ref_explored
            n_test -= 1
            if n_test == 0:
                break

    def same_node_bi_test(self, graph, method, n_test=10, **kwargs):
        keys = list(networkx.connected_components(graph).next())
        random.shuffle(keys)
        for i in range(n_test):
            path = method(graph, keys[i], keys[i], **kwargs)
            assert path == []

    def test_same_node_bi(self):
        self.same_node_bi_test(self.romania, breadth_first_search)
        self.same_node_bi_test(self.romania, uniform_cost_search)
        self.same_node_bi_test(self.romania, a_star, heuristic=null_heuristic)
        self.same_node_bi_test(self.romania, a_star,
                               heuristic=euclidean_dist_heuristic)
        self.same_node_bi_test(self.romania, bidirectional_ucs,
                               heuristic=euclidean_dist_heuristic)
        self.same_node_bi_test(self.romania, bidirectional_a_star,
                               heuristic=null_heuristic)
        self.same_node_bi_test(self.romania, bidirectional_a_star,
                               heuristic=euclidean_dist_heuristic)

    def test_bfs_romania(self):
        self.romania_test(self.reference_bfs_path, breadth_first_search)

    def test_ucs_romania(self):
        self.romania_test(self.reference_path, uniform_cost_search)

    def test_a_star_null_romania(self):
        self.romania_test(self.reference_path, a_star, heuristic=null_heuristic)

    def test_a_star_euclidean_romania(self):
        self.romania_test(self.reference_path, a_star,
                          heuristic=euclidean_dist_heuristic)

    def test_bi_ucs_romania(self):
        self.romania_test(self.reference_path, bidirectional_ucs)

    def test_bi_ucs_atlanta(self):
        # put n_test = -1 to run forever until it breaks
        self.atlanta_bi_test(bidirectional_ucs, n_test=10)

    def test_bi_a_star_null_romania(self):
        self.romania_test(self.reference_path, bidirectional_a_star,
                          heuristic=null_heuristic)

    def test_bi_a_star_null_atlanta(self):
        # put n_test = -1 to run forever until it breaks
        self.atlanta_bi_test(bidirectional_a_star, heuristic=null_heuristic,
                             n_test=10)

    def test_bi_a_star_euclidean_romania(self):
        self.romania_test(self.reference_path, bidirectional_a_star,
                          heuristic=euclidean_dist_heuristic)

    def test_bi_a_star_euclidean_atlanta(self):
        # put n_test = -1 to run forever until it breaks
        self.atlanta_bi_test(bidirectional_a_star,
                             heuristic=euclidean_dist_heuristic, n_test=10)


if __name__ == '__main__':
    unittest.main()