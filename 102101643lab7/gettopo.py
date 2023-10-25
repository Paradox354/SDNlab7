#!/usr/bin/python
import requests
from requests.auth import HTTPBasicAuth
def http_get(url):
    url= url
    headers = {'Content-Type':'application/json'}
    resp = requests.get(url,headers=headers,auth=HTTPBasicAuth('admin', 'admin'))
    return resp

if __name__ == "__main__":
    url = 'http://127.0.0.1:8181/restconf/operational/network-topology:network-topology'
    resp = http_get(url)
    print (resp.content)

