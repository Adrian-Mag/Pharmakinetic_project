import unittest
import sys
sys.path.append('../')
from protocol import Protocol


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
        my_protocol = Protocol(end_time, points, intervals, spikes)
        self.assertEqual(my_protocol.value(0.1), 1)
        
if __name__ == '__main__':
    unittest.main()

