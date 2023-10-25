import tkinter as tk
from PIL import Image, ImageTk
import subprocess
import threading
import signal

def run_script(command):
    subprocess.call(command)

def display_topology():
    image_path = "/home/pvv/SDN/102101643lab7/1697966896074.png"  # 替换为你的拓扑图片路径
    image = Image.open(image_path)
    photo = ImageTk.PhotoImage(image)
    image_label.config(image=photo)
    image_label.image = photo
    text_area.delete('1.0', tk.END)
    text_area.insert(tk.END, "拓扑2图片显示中...")

    # 假设在这里执行显示拓扑图片的代码
    # 可以使用PIL库加载图片并在image_label中显示

def build_topology_1():
    command = ['sudo', 'mn', '--topo=single,3', '--mac', '--controller=remote,ip=127.0.0.1,port=6633', '--switch', 'ovsk,protocols=OpenFlow13']
    thread = threading.Thread(target=run_script, args=(command,))
    thread.start()

def build_topology_2():
    command = ['sudo', 'mn', '--custom', 'topo.py', '--topo', 'mytopo', '--mac', '--controller=remote,ip=127.0.0.1,port=6633', '--switch', 'ovsk,protocols=OpenFlow13']
    thread = threading.Thread(target=run_script, args=(command,))
    thread.start()
def disable_ctrl_c(signal, frame):
    print("Ctrl+C被禁用")

# 注册Ctrl+C信号的处理函数
signal.signal(signal.SIGINT, disable_ctrl_c)
def delete_flow_entries():
    command = 'curl -X DELETE http://127.0.0.1:8080/stats/flowentry/clear/1; curl -X DELETE http://127.0.0.1:8080/stats/flowentry/clear/2'
    subprocess.call(['gnome-terminal', '--', 'bash', '-c', command])
    text_area.insert(tk.END, "删除流表成功！")

def distribute_flow_tables():
    subprocess.Popen(['python', 'ryu_vlan.py'])
    text_area.insert(tk.END, "下发流表成功！")

def distribute_hard_timeout_flow_tables():
    subprocess.Popen(['python', 'zhongduan.py'])  # 替换为下发硬超时流表的Python文件名
    text_area.insert(tk.END, "下发硬超时流表成功！")

def show_topology_info():
    command = ['python3', 'get.py']
    output = subprocess.Popen(command, stdout=subprocess.PIPE).communicate()[0]
    text_area.delete('1.0', tk.END)
    text_area.insert(tk.END, output)

def start_controller():
    command = ['./distribution-karaf-0.4.4-Beryllium-SR4/bin/karaf']
    subprocess.Popen(['gnome-terminal', '--', 'bash', '-c', ' '.join(command)], cwd='/home/pvv')
    text_area.insert(tk.END, "OpenDaylight控制器启动成功！")

def start_ryu_controller():
    command = ['gnome-terminal', '--', 'bash', '-c',
               'ryu-manager /home/pvv/ryu/ryu/app/ofctl_rest.py /home/pvv/ryu/ryu/app/simple_switch_13.py']
    subprocess.Popen(command)
    text_area.insert(tk.END, "Ryu控制器启动成功！")

def show_active_flow_entries():
    command = ['python', 'selec.py']  # 替换为调用另一个Python文件的命令
    output = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
    output_str = output[0].decode('utf-8') + output[1].decode('utf-8')
    text_area.delete('1.0', tk.END)
    text_area.insert(tk.END, output_str)
    
def show_topology_1_info():
    command = ['python', 'gettopo.py']  # 替换为调用另一个Python文件的命令
    output = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
    output_str = output[0].decode('utf-8') + output[1].decode('utf-8')
    text_area.delete('1.0', tk.END)
    text_area.insert(tk.END, output_str)
    
def display_topology_1():
    image_path = "/home/pvv/SDN/102101643lab7/18c385821a298224c0de4a862d41482.png"  # 替换为拓扑1图片的路径
    image = Image.open(image_path)
    photo = ImageTk.PhotoImage(image)
    image_label.config(image=photo)
    image_label.image = photo
    text_area.delete('1.0', tk.END)
    text_area.insert(tk.END, "拓扑1图片显示中...")

root = tk.Tk()
root.geometry('800x600')  # 设置窗口大小为800x600

# 拓扑1区域
frame_topology1 = tk.Frame(root)
frame_topology1.pack(side=tk.LEFT, padx=10, pady=10)

build_button_1 = tk.Button(frame_topology1, text="建立拓扑1", command=build_topology_1)
build_button_1.pack(pady=5)

get_topology_1_button = tk.Button(frame_topology1, text="获取拓扑1图片", command=display_topology_1)
get_topology_1_button.pack(pady=5)

distribute_hard_timeout_button = tk.Button(frame_topology1, text="下发硬超时流表", command=distribute_hard_timeout_flow_tables)
distribute_hard_timeout_button.pack(pady=5)

show_active_flow_entries_button = tk.Button(frame_topology1, text="显示活动流表项", command=show_active_flow_entries)
show_active_flow_entries_button.pack(pady=5)

show_topology_1_info_button = tk.Button(frame_topology1, text="显示拓扑1信息", command=show_topology_1_info)
show_topology_1_info_button.pack(pady=5)

start_controller_button = tk.Button(frame_topology1, text="启动OpenDaylight控制器", command=start_controller)
start_controller_button.pack(pady=5)

# 拓扑2区域
frame_topology2 = tk.Frame(root)
frame_topology2.pack(side=tk.RIGHT, padx=10, pady=10)

build_button_2 = tk.Button(frame_topology2, text="建立拓扑2", command=build_topology_2)
build_button_2.pack(pady=5)

show_topology_button = tk.Button(frame_topology2, text="显示拓扑2图片", command=display_topology)
show_topology_button.pack(pady=5)

delete_button = tk.Button(frame_topology2, text="删除流表项", command=delete_flow_entries)
delete_button.pack(pady=5)

distribute_button = tk.Button(frame_topology2, text="分发流表", command=distribute_flow_tables)
distribute_button.pack(pady=5)

show_info_button = tk.Button(frame_topology2, text="显示拓扑2信息", command=show_topology_info)
show_info_button.pack(pady=5)

start_ryu_button = tk.Button(frame_topology2, text="启动RYU控制器", command=start_ryu_controller)
start_ryu_button.pack(pady=5)

image_label = tk.Label(root)
image_label.pack(pady=10)

text_area = tk.Text(root)
text_area.pack(pady=10)

root.mainloop()
