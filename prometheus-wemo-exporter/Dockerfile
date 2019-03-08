FROM python:2.7

ENV CODE_DEST /opt/wemo-exporter
WORKDIR ${CODE_DEST}

COPY wemo-exporter.py ${CODE_DEST}

RUN pip install pywemo prometheus_client

EXPOSE 9801

ENTRYPOINT [ "/usr/local/bin/python", "wemo-exporter.py", "9801", "198.0.2.101" ]
