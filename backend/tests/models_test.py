import unittest
from uploader.models import ESP32FirmwareUploader

class ConnectorMock:

  def ports(self):
    pass

class StorageMock:

  def boards(self):
    pass

  def frameworks(self):
    pass

class TestModelsMethods(unittest.TestCase):

  def setUp(self):
    self.connector = ConnectorMock()
    self.storage = StorageMock()
    self.model = ESP32FirmwareUploader(self.storage, self.connector)


if __name__ == "__main__":
    unittest.main()