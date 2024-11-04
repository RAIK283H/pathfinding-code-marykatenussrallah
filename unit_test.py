import math
import unittest
import pathing
import global_game_data
import graph_data
import permutation


class TestPathFinding(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('test'.upper(), 'TEST')

    def test_isupper(self):
        self.assertTrue('TEST'.isupper())
        self.assertFalse('Test'.isupper())

    def test_floating_point_estimation(self):
        first_value = 0
        for x in range(1000):
            first_value += 1/100
        second_value = 10
        almost_pi = 3.1
        pi = math.pi
        self.assertNotEqual(first_value,second_value)
        self.assertAlmostEqual(first=first_value,second=second_value,delta=1e-9)
        self.assertNotEqual(almost_pi, pi)
        self.assertAlmostEqual(first=almost_pi, second=pi, delta=1e-1)

    def test_dfs(self):
        global_game_data.current_graph_index = 3
        global_game_data.target_node = [None, None, None, 9]
        expected = [0, 1, 2, 3, 7, 11, 10, 9, 8, 4, 0, 1, 2, 3, 7, 11, 15]
        actual = pathing.get_dfs_path()
        self.assertEqual(expected, actual)
    
    def test_bfs(self):
        global_game_data.current_graph_index = 1
        global_game_data.target_node = [None, 2]
        expected = [0, 1, 2, 3]
        actual = pathing.get_bfs_path()
        self.assertEqual(expected, actual)

    def test_hamiltonian_cycles(self):
        graph = graph_data.graph_data[0]
        n = len(graph)
        for perm in permutation.generate_permutations(n):
            path = [0] + perm + [n-1]
            actual = permutation.check_hamiltonian_cycle(graph, path)
            expected = False
            self.assertEqual(actual, expected)

    def test_hamiltonian_cycles_true(self):
        graph = graph_data.hamiltonian_cycle
        n = len(graph)
        for perm in permutation.generate_permutations(n):
            path = [0] + perm + [0]
            actual = permutation.check_hamiltonian_cycle(graph, path)
            print(f"actual: {actual}")
            expected = True
            self.assertEqual(actual, expected)



if __name__ == '__main__':
    unittest.main()
