import unittest
import pkmodel as pk
from protocol import Protocol


class SolutionTest(unittest.TestCase):
    """
    Tests the :class:`Solution` class.
    """
    def test_create(self):
        """
        Tests Solution creation.
        """
        model = {
            'name': 'model1',
            'CL': 1.0,
            'V_c': 1.0,
            'Q_p1': 1.0,
            'V_p1': 1.0,
            }
        my_protocol = Protocol('const', 5)
        my_solution = Solution(model, my_protocol)

