import unittest
import pkmodel as pk


class ProtocolTest(unittest.TestCase):
    """
    Tests the :class:`Protocol` class.
    """
    def test_create(self):
        """
        Tests Protocol creation.
        """
        model = pk.Protocol()
        self.assertEqual(model.dosing, 'const')
        self.assertEqual(model.amount, 10.0)
        self.assertEqual(model.interval, 25)

