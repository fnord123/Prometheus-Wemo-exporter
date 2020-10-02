FROM python:3

ENV CODE_DEST /opt/wemo-exporter
WORKDIR ${CODE_DEST}

COPY wemo-exporter.py ${CODE_DEST}

RUN pip install pywemo prometheus_client envargparse

EXPOSE 8000

CMD [ "python", "./wemo-exporter.py" ]
