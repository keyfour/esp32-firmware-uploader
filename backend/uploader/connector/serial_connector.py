from . import Connector
from serial.tools import list_ports

class SerialConnector(Connector):

  def ports(self):
    result = []
    ports_list = list_ports.comports()
    for port in ports_list:
      result.append(port.device)
    return result

