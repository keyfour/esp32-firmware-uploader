import unittest
import os, sys
from uploader.storage import LocalJsonStorage

if sys.platform == 'linux' or sys.platform == 'cygwin' \
  or sys.platform == 'darwin':
  TMP_DIR = os.getenv('TMPDIR', '/tmp')
else:
  TMP_DIR = os.getenv('TEMP','C:\\Temp')

class TestStorageMethods(unittest.TestCase):

  VALID_JSON = '{"board": "ESP32", "name": "Device", "start":0}'

  def setUp(self):
    self.path_prefix = TMP_DIR
    self.local_json_storage = LocalJsonStorage(self.path_prefix)
    self.valid_json = self.VALID_JSON
    self.invalid_json = self.valid_json.replace('"','\\"')
    self.valid_json_path = self.path_prefix + '/valid.json'
    self.invalid_json_path = self.path_prefix + '/invalid.json'

  def test_local_json_storage_paths(self):
    self.assertEqual(self.path_prefix + '/boards.json',
      self.local_json_storage.boards_file)
    self.assertEqual(self.path_prefix + '/frameworks.json',
      self.local_json_storage.frameworks_file)

  def test_local_json_storage_parse_file(self):
    with open(self.valid_json_path, "w") as f:
      f.write(self.valid_json)
    with open(self.invalid_json_path, "w") as f:
      f.write(self.invalid_json)
    result = self.local_json_storage.parse_file(self.valid_json_path)
    self.assertTrue(isinstance(result, dict))
    self.assertEqual(result['board'], "ESP32")
    self.assertEqual(result['name'], "Device")
    self.assertEqual(result['start'], 0)
    result = self.local_json_storage.parse_file(self.invalid_json_path)
    self.assertTrue(isinstance(result, dict))
    self.assertEqual(len(result), 0)

  def tearDown(self):
    if os.path.isfile(self.valid_json_path):
      os.remove(self.valid_json_path)
    if os.path.isfile(self.invalid_json_path):
      os.remove(self.invalid_json_path)

