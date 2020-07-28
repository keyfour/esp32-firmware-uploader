from operator import itemgetter, methodcaller

class ESP32FirmwareUploader:

    def __init__(self, storage, connector):
        self.storage = storage
        self.connector = connector
        self.board = None
        self.framework = None
        self.port = None
        self.files = None
        self.boards_list = []
        self.frameworks_list = []
        self.ports_list = []

    def from_storage(self, method):
        result = None
        if self.storage is not None:
            getter = getattr(self.storage, method)
            result = getter()
        return result

    def boards(self):
        if len(self.boards_list) == 0:
            self.boards_list = self.from_storage("boards")
        return self.boards_list

    def frameworks(self):
        if len(self.frameworks_list) == 0:
            self.frameworks_list = self.from_storage("frameworks")
        return self.frameworks_list

    def ports(self):
        if self.connector is not None:
            self.ports_list = self.connector.ports()
        return self.ports_list

    def select(self, board_id, framework_id):
        indexes, boards = self.get_items(self.boards)
        if boards is not None and board_id in indexes:
            self.board = boards[indexes.index(board_id)]
        indexes, frameworks = self.get_items(self.frameworks)
        if frameworks is not None and framework_id in indexes:
            self.framework = frameworks[indexes.index(framework_id)]

        result = False
        if self.board is not None and \
          self.framework is not None:
            result = True
        return result

    def get_items(self, method):
        items = method()
        indexes = self.indexes(items)
        return indexes, items

    def indexes(self, items):
        index = itemgetter('id')
        return list(map(index, items))

    def open(self, port):
        result = False
        if self.ports() is not None and \
          port in self.ports():
            self.port = port
            result = True
        return result

    def upload(self):
        pass
