import unittest
from equation import resolution


class Tests(unittest.TestCase):

    def test_resolution_inputs_error(self):
        self.assertEqual(resolution(1, 2, 'a'), None)

    def test_resolution_imputs_0(self):
        self.assertEqual(resolution(0, 0, 0), None)

    def test_resolution_delta_negative(self):
        self.assertEqual(resolution(1, 1, 1), [0, {}])

    def test_resolution_delta_0(self):
        self.assertEqual(resolution(1, 2, 1), [1, {-1.0}])

    def test_resolution_delta_positive(self):
        self.assertEqual(resolution(1, 4, 1), [2, {-0.2679491924311228, -3.732050807568877}])

    def test_resolution_bc_not_0(self):
        self.assertEqual(resolution(0, 4, 1), [1, {-0.25}])

    def test_resolution_ab_not_0(self):
        self.assertEqual(resolution(2, 4, 0), [2, {0.0, -2.0}])

    def test_resolution_bc_is_0_and_a_is_0(self):
        self.assertEqual(resolution(0, 0, 1), [0, {}])

    # def test_resolution_ac_equal_0(self):
    #     self.assertEqual(resolution(1, 0, 1), [0, {}])


unittest.main()
