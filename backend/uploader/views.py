from uploader import app
from flask import jsonify

from .models import ESP32FirmwareUploader
from .storage import LocalJsonStorage
from .connector import SerialConnector

storage = LocalJsonStorage('./data')
connector = SerialConnector()
model = ESP32FirmwareUploader(storage, connector)

@app.route('/')
def index():
  return ''

@app.route('/boards')
def boards():
  return jsonify(model.boards())

@app.route('/frameworks')
def frameworks():
  return jsonify(model.frameworks())

@app.route('/ports')
def ports():
  return jsonify(model.ports())