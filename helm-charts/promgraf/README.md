(Execute these commands from the parent directory)

To install:

1. Make sure `/var/prometheus/data` exists
2. Edit `values.yaml` to set IP addresses and data sources as neccessary.
3. Remove any dashboards you don't want from `templates/020-dashboard.yaml`
4. `helm dep update promgraf`
5. `helm install -n promgraf promgraf`

To upgrade:

1. `helm dep update promgraf`
2. `helm upgrade --recreate-pods promgraf promgraf`

To connect to web UI:

1. Prometheus will be on port 31300
2. Grafana will be on port 30301. See password in values.yaml

To backup the data:

1. `curl -XPOST http://<local-machine-public-ip-address>:31301/api/v1/admin/tsdb/snapshot`
2. Find the snapshot in `/var/prometheus/data/snapshots`, tarball it, and rm it.