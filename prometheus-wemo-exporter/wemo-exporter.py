# Prometheus Wemo Exporter
#
# Scott Baker
# http://www.smbaker.com/

from prometheus_client import start_http_server, Metric, REGISTRY
import pywemo
import sys
import time

class WemoCollector(object):
  def __init__(self, wemo_ip):
      self._wemo_ip = wemo_ip
      self._wemo_port = pywemo.ouimeaux_device.probe_wemo(self._wemo_ip)
      self._wemo_url = 'http://%s:%i/setup.xml' % (self._wemo_ip, self._wemo_port)

  def collect(self):
    device = pywemo.discovery.device_from_description(self._wemo_url, None)

    # Convert requests and duration to a summary in seconds
    metric = Metric('today_kwh', "Kilowatt-hours today", 'gauge')
    metric.add_sample("today_kwh", value=device.today_kwh, labels = {})
    yield metric

    metric = Metric('today_on_time', "Today on time", 'gauge')
    metric.add_sample("today_on_time", value=device.today_on_time, labels = {})
    yield metric

    metric = Metric('today_standby_time', "Today standby time", 'gauge')
    metric.add_sample("today_standby_time", value=device.today_standby_time, labels = {})
    yield metric

    metric = Metric('current_power', "Current watts", 'gauge')
    metric.add_sample("current_power", value=device.current_power, labels = {})
    yield metric

    metric = Metric('threshold_power', "Threshold power", 'gauge')
    metric.add_sample("threshold_power", value=device.threshold_power, labels = {})
    yield metric

    metric = Metric('state', "State", 'gauge')
    metric.add_sample("state", value=device.get_state(), labels = {})
    yield metric

if __name__ == '__main__':
  if len(sys.argv)<3:
      print >> sys.stderr, "Syntax: wemo_exporter.py <port> <ip>"

  start_http_server(int(sys.argv[1]))
  REGISTRY.register(WemoCollector(sys.argv[2]))

  while True: time.sleep(1)
