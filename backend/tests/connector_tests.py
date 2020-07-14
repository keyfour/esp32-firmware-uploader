import unittest
from uploader.connector import SerialConnector

class TestConnectorMethods(unittest.TestCase):

  def setUp(self):
    self.connector = SerialConnector()

  def test_ports_returns_list(self):
    self.assertTrue(isinstance(self.connector.ports(), list))


if __name__ == "__main__":
    unittest.main()