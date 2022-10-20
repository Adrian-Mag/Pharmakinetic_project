import unittest
import pkmodel as pk


class ModelTest(unittest.TestCase):
    """
    Tests the :class:`Model` class.
    """
    def test_create(self):
        """
        Tests Model creation.
        """
        model = pk.Model(1.0, 2.0, 2.5, 3.0, 3.5, 4.0, 5.0)
        dict_of_params = model.construct_param_dict()
        assert type(dict_of_params) == dict
        assert dict_of_params['V_c'] == 1.0
        assert dict_of_params['K_a'] == 2.5
        assert dict_of_params['V_p2'] == 5.0

