# Prometheus Wemo Exporter
#
# Scott Baker
# http://www.smbaker.com/

#from prometheus_client import start_http_server, Metric, REGISTRY
from prometheus_client import start_http_server, Gauge
import requests
import pywemo
import sys
from time import sleep
from envargparse import EnvArgParser, EnvArgDefaultsHelpFormatter

class wemoInfluxdbExporter:
  def __init__(self):
    try:
      self._args = {}
      # self._interval = 15
      # self._wemo_ip = ""
      # self._wemo_port = 0
      # self._influxdb_ip = ""
      # self._influxdb_port = 8086
      # self._influxdb_database = ""
      self.main()
    except Exception as e:
      print('Error - {}'.format(e))
      sys.exit(1)

  def process_args(self):
    parser = EnvArgParser\
          ( prog="Wemo Influxdb Exporter"
          , formatter_class=EnvArgDefaultsHelpFormatter
          )
    parser.add_argument\
        ( '--interval'
        , required=False
        , env_var="INTERVAL"
        , type=int
        , nargs="?"
        , default=15
        , help="How often data should be pulled from the Wemo and exported to influxdb"
        )
    parser.add_argument\
        ( '--wemo_ip'
        , required=True
        , env_var="WEMO_IP"
        , nargs="?"
        , default="localhost"
        , help="IP address for the Wemo to pull data from"
        )
    parser.add_argument\
        ( '--wemo_device'
        , required=False
        , env_var="WEMO_DEVICE"
        , nargs="?"
        , default="Wemo Insight"
        , help="name of the Wemo device being queried"
        )
    parser.add_argument\
        ( '--port'
        , required=True
        , env_var="EXPORTER_PORT"
        , type=int
        , nargs="?"
        , help="Port number the exporter should bind to"
        )

    self._args = parser.parse_args()
    print(self._args)

  def collect(self):
    device = pywemo.discovery.device_from_description( \
      self._wemo_url, None)
    self._power.labels(self._args.wemo_device) \
      .set(device.current_power)
    self._today_kwh.labels(self._args.wemo_device) \
      .set(device.today_kwh)
    self._today_on_time.labels(self._args.wemo_device) \
      .set(device.today_on_time)
    self._today_standby_time.labels(self._args.wemo_device) \
      .set(device.today_standby_time)

  def main(self):
    self.process_args()
    self._wemo_port = pywemo.ouimeaux_device.probe_wemo(self._args.wemo_ip)
    self._wemo_url = 'http://%s:%i/setup.xml' \
      % (self._args.wemo_ip, self._wemo_port)
    self._power = \
      Gauge('power', 'Instantaneous power consumption', ['device'])
    self._today_kwh =\
       Gauge('today_kwh', 'kWh consumed since midnight', ['device'])
    self._today_on_time = \
      Gauge('today_on_time', 'On time since midnight', ['device'])
    self._today_standby_time = \
      Gauge('today_standby_time', 'Off time since midnight', ['device'])
    start_http_server(self._args.port)
    while True:
      self.collect()
      sleep(self._args.interval)

wemoInfluxdbExporter()
