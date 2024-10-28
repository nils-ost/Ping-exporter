# Ping-exporter
Simple Grafana-Prometheus exporter to ping Servers

## Setup Dev-Environment

On your workstation check-out this repo, `cd` into it and execute the following commands:

```
sudo apt update; sudo apt install python3 virtualenv direnv
virtualenv -p /usr/bin/python3 venv
venv/bin/pip install -r requirements.txt
venv/bin/pre-commit install
sed -nr '/direnv hook bash/!p;$aeval "\$(direnv hook bash)"' -i ~/.bashrc
source ~/.bashrc
echo -e "source venv/bin/activate\nunset PS1" > .envrc
direnv allow
```


## Starting Exporter

The easiest way to start the exporter via docker, like shown in the example `docker-compose.yml`

You just need one instance of this exporter to ping a bunch of hosts, as shown in the following Prometheus example:


## Example Prometheus Config

```
scrape_configs:
  - job_name: 'ping'
    static_configs:
      - targets: ['192.168.1.1']
        labels:
          server: 'router'
      - targets: ['192.168.1.2']
        labels:
          server: 'dns'
      - targets: ['192.168.1.3']
        labels:
          server: 'switch'
    metrics_path: /ping
    relabel_configs:
      - source_labels: [__address__]
        target_label: __param_host
      - source_labels: [__param_host]
        target_label: instance
      - target_label: __address__
        replacement: 192.168.1.7:8080  # The ping exporter's real hostname:port
```
