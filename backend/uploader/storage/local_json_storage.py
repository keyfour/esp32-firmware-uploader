from . import Storage
import json

class LocalJsonStorage(Storage):

  def __init__(self, path):
    self.boards_file = path + "/boards.json"
    self.frameworks_file = path + "/frameworks.json"

  def parse_file(self, path):
    result = {}
    with open(path) as file:
      data = file.read()
    if len(data) > 0:
      try:
        result = json.loads(data)
      except json.decoder.JSONDecodeError:
        pass
    return result

  def boards(self):
    return self.parse_file(self.boards_file)

  def frameworks(self):
    return self.parse_file(self.frameworks_file)