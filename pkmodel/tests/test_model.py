import unittest
import pkmodel as pk


class ModelTest(unittest.TestCase):
    """
    Tests the :class:`Model` class.
    """
    def test_create(self):
        """
        Tests Model creation and attributes.
        """
        model1 = pk.Model(1.0, 2.0, 2.5, 3.0, 3.5, 4.0, 5.0)
        model2 = pk.Model(2.0, 1.0, Q_p1=3.0, V_p1=4.0)
        assert model1.subcutaneous == 1
        assert model1.peripherals == 2
        assert model2.subcutaneous == 0
        assert model2.peripherals == 1
        with self.assertRaises(AssertionError):
            assert len(model1.Qp) == 3
            assert len(model2.Vp) == 2
            assert model1.Vc == 2.0
            assert model2.CL == 2.0

