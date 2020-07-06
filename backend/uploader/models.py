
class ESP32FirmwareUploader:

    def __init__(self, storage, connector):
        self.storage = storage
        self.connector = connector
        self.board = None
        self.framework = None
        self.port = None
        self.files = None

    def from_storage(self, method):
        result = None
        if self.storage() is not None:
            getter = getattr(self.storage, method)
            result = getter()
        return result

    def boards(self):
        return self.from_storage("boards")

    def frameworks(self):
        return self.from_storage("frameworks")

    def ports(self):
        available_ports = None
        if self.connector is not None:
            available_ports = self.connector.ports()
        return available_ports

    def select(self, board, framework):
        if self.boards() is not None and \
          board in self.boards():
            self.board = board
        if self.frameworks() is not None and \
          framework in self.frameworks():
            self.framework = framework

        result = False
        if self.board is not None and \
          self.framework is not None:
            result = True
        return result

    def open(self, port):
        result = False
        if self.ports() is not None and \
          port in self.ports():
            self.port = port
            result = True
        return result

    def upload(self):
        pass
