from . import Connector
import serial

class SerialConnector(Connector):

  def ports(self):
    result = []
    ports_list = serial.tools.list_ports.comports()
    for port in ports_list:
      result.append(port.device)
    return result

