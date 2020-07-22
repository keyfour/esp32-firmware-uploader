import unittest
from uploader.models import ESP32FirmwareUploader

PORTS = [
        {
          'id': 0,
          'name': '/dev/ttyUSB0',
        },
        {
          'id': 1,
          'name': '/dev/ttyACM0',
        },
        {
          'id': 2,
          'name': '/dev/ttyS0',
        }]

BOARDS = [
        {
          'id': 0,
          'name': 'ESP32-WROOM',
        },
        {
          'id': 1,
          'name': 'ESP32-CAM',
        },
        {
          'id': 2,
          'name': 'Heltec ESP32s',
        },
      ]

FRAMEWORKS = [
        {
          'id': 0,
          'name': 'Arduino',
        },
        {
          'id': 1,
          'name': 'ESP-IDF',
        },
      ]

class ConnectorMock:

  def __init__(self):
    self.is_empty = False

  def ports(self):
    if not self.is_empty:
      return PORTS
    else:
      return []

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

  def test_ports_return_correct(self):
    self.connector.is_empty = False
    ports = self.model.ports()
    self.assertTrue(isinstance(ports, list))
    self.assertEqual(len(ports), len(PORTS))
    for i, port in enumerate(ports):
      self.assertEqual(port['id'], PORTS[i]['id'])
      self.assertEqual(port['name'], PORTS[i]['name'])

  def test_ports_return_empty(self):
    self.connector.is_empty = True
    ports = self.model.ports()
    self.assertTrue(isinstance(ports, list))
    self.assertEqual(len(ports), 0)

if __name__ == "__main__":
    unittest.main()