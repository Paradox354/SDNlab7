import requests
import time
import re


class GetNodes:
    def __init__(self, ip):
        self.ip = ip
        
    def get_switch_id(self):
        url = 'http://' + self.ip + '/stats/switches'
        re_switch_id = requests.get(url=url).json()
        switch_id_hex = []
        for i in re_switch_id:
            switch_id_hex.append(hex(i))

        return switch_id_hex

    def getflow(self):
        url = 'http://' + self.ip + '/stats/flow/%d'
        switch_list = self.get_switch_id()
        ret_flow = []
        for switch in switch_list:
            new_url = format(url % int(switch, 16))
            re_switch_flow = requests.get(url=new_url).json()
            ret_flow.append(re_switch_flow)
        return ret_flow

    def show(self):
        flow_list = self.getflow()
        for flow in flow_list:
            for dpid in flow.keys():
                dp_id = dpid
                switchnum= '{1}'.format(hex(int(dp_id)), int(dp_id))        
                print('s'+switchnum,end = " ")
                switchnum = int(switchnum)
            for list_table in flow.values():
                for table in list_table:         
                    string1 = str(table)
                    if re.search("'dl_vlan': '(.*?)'", string1) is not None:
                       num = re.search("'dl_vlan': '(.*?)'", string1).group(1);
                       if num == '0' and switchnum == 1:
                          print('h1',end = " ")
                          print('(h1--s'+str(switchnum)+')')
                       if num == '1' and switchnum == 1:
                          print('h2',end = " ")
                          print('(h2--s'+str(switchnum)+')')
                       if num == '0' and switchnum == 2:
                          print('h3',end = " ")
                          print('(h3--s'+str(switchnum)+')')
                       if num == '1' and switchnum == 2:
                          print('h4',end = " ")
                          print('(h4--s'+str(switchnum)+')')
        print('s1--s2')
        print("")
        flow_list = self.getflow()
        for flow in flow_list:
            for dpid in flow.keys():
                dp_id = dpid
                print('switch_name:s{1}'.format(hex(int(dp_id)), int(dp_id)))
            for list_table in flow.values():
                for table in list_table:
                    print(table)
s1 = GetNodes("127.0.0.1:8080")
s1.show()

