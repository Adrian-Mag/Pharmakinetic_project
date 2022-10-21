import unittest
import numpy as np
import pkmodel as pk


class ProtocolTest(unittest.TestCase):
    """
    Tests the :class:`Protocol` class.
    """
    def test_create(self):
        """
        Tests Protocol creation.
        """
        end_time = 1
        points = 101
        intervals = [{'start': 0, 'end': 0.1, 'dose': 1},
                     {'start': 0.5, 'end': 0.6, 'dose': 1},
                     {'start': 0.9, 'end': 1, 'dose': 2}]
        spikes = [{'time': 0.2, 'dose': 1},
                  {'time': 0.8, 'dose': 2}]
        my_protocol = pk.Protocol('protocol1', end_time, points,
                                  intervals, spikes)

        assert ((my_protocol.time == np.linspace(0, 1, 101)).all())
        self.assertEqual(my_protocol.value(0.1), 1)
        self.assertEqual(my_protocol.value(0.2), 100)
        self.assertEqual(my_protocol.value(0.8), 200)
        self.assertEqual(my_protocol.value(0.82), 0)


if __name__ == '__main__':
    unittest.main()
