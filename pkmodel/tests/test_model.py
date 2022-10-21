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
        model1 = {'name': 'model_test',
                  'CL': 1.0,
                  'Vc': 2.0,
                  'ka': 10.0,
                  'Qp1': 3.0,
                  'Vp1': 4.0,
                  'Qp2': 5.6,
                  'Vp2': 7.98948
                  }

        test_model = pk.Model(model1)
        assert (test_model.name == 'model_test')
        assert (test_model.CL == 1)
        assert (test_model.Vc == 2)
        assert (test_model.Qp == [3, 5.6])
        assert (test_model.Vp == [4, 7.98948])
        assert (test_model.ka == 10)
        assert (test_model.peripherals == 2)
        assert (test_model.subcutaneous == 1)

        model2 = {'name': 5,
                  'CL': 1,
                  'Vc': 2,
                  'ka': 10,
                  'Qp1': 3,
                  'Vp1': 4,
                  'Qp2': 5,
                  'Vp2': 7
                  }

        with self.assertRaises(ValueError):
            _ = pk.Model(model2)


if __name__ == '__main__':
    unittest.main()
