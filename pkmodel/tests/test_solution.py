import unittest
import pkmodel as pk
import numpy as np


class SolutionTest(unittest.TestCase):
    """
    Tests the :class:`Solution` class.
    """
    def test_create(self):
        """
        Tests Solution creation.
        """
        # Define models--------------------------
        model1 = {'name': 'model1',
                  'CL': 1.0,
                  'Vc': 2.0,
                  'ka': 10.0,
                  'Qp1': 3.0,
                  'Vp1': 4.0}
        model2 = {'name': 'model2',
                  'CL': 1.0,
                  'Vc': 1.0,
                  'Qp1': 1.0,
                  'Vp1': 1.0}

        # Define protocol elements---------------
        end_time = 1
        points = 101

        # Build protocols-----------------------
        # Protocol 0 (constant 0)
        protocol_zero = pk.Protocol('protocol 0', end_time, points)

        # Build models--------------------------
        # Subcutaneous model with 1 peripheral
        my_model1 = pk.Model(model1)
        # Intravenous model with 1 peripheral
        my_model2 = pk.Model(model2)

        # Solve models with chosen protocols-----
        Solution_subcutaneous_0 = pk.Solution(my_model1, protocol_zero)
        Solution_intravenous_0 = pk.Solution(my_model2, protocol_zero)

        # Check solutions-----------------------
        # Check if zero protocols give back zero dosages
        assert ((np.array(Solution_subcutaneous_0.solution.y)
                == np.zeros((3, points))).all())
        assert ((np.array(Solution_intravenous_0.solution.y)
                == np.zeros((2, points))).all())


if __name__ == '__main__':
    unittest.main()
