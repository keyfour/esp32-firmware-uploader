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

  def __init__(self):
    self.is_empty = False

  def boards(self):
    if not self.is_empty:
      return BOARDS
    else:
      return []

  def frameworks(self):
    if not self.is_empty:
      return FRAMEWORKS
    else:
      return []

class TestModelsMethods(unittest.TestCase):

  def setUp(self):
    self.connector = ConnectorMock()
    self.storage = StorageMock()
    self.model = ESP32FirmwareUploader(self.storage, self.connector)
    self.list_keys = ["id", "name"]

  def test_ports_return_correct(self):
    self.connector.is_empty = False
    ports = self.model.ports()
    self.compare_lists(ports, PORTS, self.list_keys)

  def test_ports_return_empty(self):
    self.connector.is_empty = True
    ports = self.model.ports()
    self.compare_lists(ports, [])

  def tets_boards_return(self):
    self.storage.is_empty = False
    boards = self.model.boards()
    self.compare_lists(boards, BOARDS, self.list_keys)

  def test_boards_return_empty(self):
    self.storage.is_empty = True
    boards = self.model.boards()
    self.compare_lists(boards, [])

  def test_frameworks_return(self):
    self.storage.is_empty = False
    frameworks = self.model.frameworks()
    self.compare_lists(frameworks, FRAMEWORKS, self.list_keys)

  def test_frameworks_return_empty(self):
    self.storage.is_empty = True
    frameworks = self.model.frameworks()
    self.compare_lists(frameworks, [])


  def compare_lists(self, list0, list1, keys=[]):
    self.assertTrue(isinstance(list0, list))
    self.assertTrue(isinstance(list1, list))
    self.assertEqual(len(list0), len(list1))
    for item0, item1 in zip(list0, list1):
      for key in keys:
        self.assertEqual(item0[key], item1[key])

if __name__ == "__main__":
    unittest.main()