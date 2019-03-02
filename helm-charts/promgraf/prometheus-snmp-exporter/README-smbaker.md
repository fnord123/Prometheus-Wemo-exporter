Nasty Ugly Mess regarding setting snmp.yml in this helm chart.

I couldn't get the "config" variable to work right, it always indented it in the config map by two extra spaces.

`{{ .Values.config | indent 4 }}` instead of `{{ toYaml .Values.config | indent 4 }}` in the configmap template worked, but
still required annoying use of `--set`.

So I just used a `.Files.Get` instead.
