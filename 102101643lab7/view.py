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
        num_host=3
        host_macs = set()  # 用于存储不同的主机MAC地址
        #print(flow_list)
        for entry in flow_list:
            match = entry.get('match', {})
            src_mac = match.get('dl_src')
            dst_mac = match.get('dl_dst')
            if src_mac is not None:
               host_macs.add(src_mac)
            if dst_mac is not None:
               host_macs.add(dst_mac)
        num_hosts = len(host_macs)
        print("拓扑中的主机数量：", num_host)
        for flow in flow_list:
            for dpid in flow.keys():
                dp_id = dpid
                switchnum= '{1}'.format(hex(int(dp_id)), int(dp_id))        
                print('s'+switchnum,end = " ")
                switchnum = int(switchnum)
            print("\nlink:")
            i = 1
            while i <= num_host:
                print('s1--h'+str(i))
                i+=1
            for list_table in flow.values():
                for table in list_table:         
                    string1 = str(table)
                    if re.search("'dl_vlan': '(.*?)'", string1) is not None:
                       num = re.search("'dl_vlan': '(.*?)'", string1).group(1);
                       if num == '0' and switchnum == 1:
                          print('h1',end = " ")
                       if num == '1' and switchnum == 1:
                          print('h2',end = " ")
                       if num == '0' and switchnum == 2:
                          print('h3',end = " ")
                       if num == '1' and switchnum == 2:
                          print('h4',end = " ")
        print("\n")
        flow_list = self.getflow()
        print("h1 h2 h3")
        for flow in flow_list:
            for dpid in flow.keys():
                dp_id = dpid
                print('switch_name:s{1}'.format(hex(int(dp_id)), int(dp_id)))
            for list_table in flow.values():
                for table in list_table:
                    print(table)
s1 = GetNodes("127.0.0.1:8080")
s1.show()

