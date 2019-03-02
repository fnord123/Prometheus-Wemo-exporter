# Various Helm Charts #

Scott Baker, http://www.smbaker.com/

This directory contains various helm charts for bringing up services. Some of these services are used by multiple projects.

## List of Charts ##

* **promgraf**: Monitoring using Prometheus and Grafana.

  * Contains dashboards `envmon`, `3d printer`, `power`
  * Used by repositories `envmon` and `octoprint-prometheus`

  This chart is my monitoring infrastructure for my home office. It is setup to monitor several different device, so people looking to monitor just one of these devices should be prepared to comment out the unwanted dashboards (`promgraf/templates/020-dashboards.yaml`) and the unwanted scrapers (`promgraf/values.yaml). 

  This first device is my environmental/air-quality monitors. These use a handful of sensors to measure temperature, humidity, dust, chemicals, etc. 

  The second device is my Prusa I3 Mk3 printer, running OctoPrint. I developed a custom plugin that provides a prometheus interface to OctoPrint. This reports filament used, temperatures, printer state, filenames, etc.

  The third device is an APC smart ups with network management card. This shows the voltage and current for the primary server computer that I use. It makes use of an exporter, `prometheus-snmp-exporter` to query the UPS via SNMP and report the information to prometheus.

