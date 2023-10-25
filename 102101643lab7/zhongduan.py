#!/usr/bin/python
import requests
from requests.auth import HTTPBasicAuth
def http_put(url,jstr):
    url= url
    headers = {'Content-Type':'application/json'}
    resp = requests.put(url,jstr,headers=headers,auth=HTTPBasicAuth('admin', 'admin'))
    return resp

if __name__ == "__main__":
    url = 'http://127.0.0.1:8181/restconf/config/opendaylight-inventory:nodes/node/openflow:1/flow-node-inventory:table/0/flow/1'
    with open("flowstable.json") as f:
        jstr = f.read()
    resp = http_put(url,jstr)
    print (resp.content)

