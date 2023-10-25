#!/usr/bin/python
import requests
from requests.auth import HTTPBasicAuth
def http_get(url):
    url= url
    headers = {'Content-Type':'application/json'}
    resp = requests.get(url,headers=headers,auth=HTTPBasicAuth('admin', 'admin'))
    print (resp.content)
    url = 'http://127.0.0.1:8181/restconf/config/opendaylight-inventory:nodes/node/openflow:1/flow-node-inventory:table/0/flow/1'
    resp = requests.put(url,jstr,headers=headers,auth=HTTPBasicAuth('admin', 'admin'))
    print (resp.content)
    url= url
    headers = {'Content-Type':'application/json'}
    resp = requests.get(url,headers=headers,auth=HTTPBasicAuth('admin', 'admin'))
    print (resp.content)
    return resp

if __name__ == "__main__":
    url = 'http://127.0.0.1:8181/restconf/operational/opendaylight-inventory:nodes/node/openflow:1/flow-node-inventory:table/0/opendaylight-flow-table-statistics:flow-table-statistics'
 
    with open("flowstable.json") as f:
        jstr = f.read()
    resp = http_get(url)

