container:
	docker build . -t dputzolu/wemo-exporter:latest

push: container
	docker push dputzolu/wemo-exporter:latest
