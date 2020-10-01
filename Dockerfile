FROM python:3

ENV CODE_DEST /opt/wemo-exporter
WORKDIR ${CODE_DEST}

COPY wemo-exporter.py ${CODE_DEST}

RUN pip install pywemo prometheus_client

EXPOSE 8000

CMD [ "python", "./wemo-exporter.py" ]

ENTRYPOINT [ "/usr/local/bin/python", "wemo-exporter.py", "--port=8000", "--wemo_ip 198.168.86.53", "--wemo_device='Refrigertor'"]
