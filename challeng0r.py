import requests
import subprocess

dls = "https://dashboard.nexmo.com/download_pricing"

resp = requests.get(dls)

with open('test.xls', 'wb') as output:
    output.write(resp.content)



