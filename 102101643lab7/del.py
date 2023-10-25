#!/usr/bin/python
import requests
from requests.auth import HTTPBasicAuth

def http_delete(url):
    url= url
    headers = {'Content-Type':'application/json'}
    resp = requests.delete(url,headers=headers,auth=HTTPBasicAuth('admin', 'admin'))
    return resp 

if __name__ == "__main__":
    url = 'http://127.0.0.1:8181/restconf/config/opendaylight-inventory:nodes/node/openflow:1/'
    resp = http_delete(url)
    print (resp.content)

