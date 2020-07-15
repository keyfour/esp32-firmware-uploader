import unittest
from uploader.connector import SerialConnector

class TestConnectorMethods(unittest.TestCase):

  def setUp(self):
    self.connector = SerialConnector()

  def test_ports_returns_list(self):
    ports = self.connector.ports()
    self.assertTrue(isinstance(ports, list))


if __name__ == "__main__":
    unittest.main()