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
        protocol = pk.Protocol()
        self.assertEqual(protocol.amount, 10.0)
        self.assertEqual(protocol.interval, None)

    def test_dose(self):
        """
        Tests the dose() function of the Protocol class
        """
        protocol_1 = pk.Protocol(amount=15.0)
        protocol_2 = pk.Protocol(amount=5.0, interval=100)
        self.assertEqual(protocol_1.interval, None)
        self.assertEqual(protocol_2.interval, 100)
        self.assertEqual(protocol_1.amount, 15.0)
        self.assertEqual(protocol_2.amount, 5.0)
        self.assertEqual(protocol_1.dose(), 15.0)
        self.assertEqual(protocol_2.dose(), 0)
