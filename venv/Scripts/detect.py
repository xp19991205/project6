import socket
import time
from datetime import datetime
def is_connected(url):
    try:
        host = socket.gethostbyname(url)
        s = socket.create_connection((host, 80), 2)
        return True
    except Exception as e:
        return False
URL1 ="www.baidu.com"   #检测外网连通情况
URL2 ="www.cqupt.edu.cn" #检查内网连通情况
a=is_connected(URL1)
b=is_connected(URL2)
file_name = 'write.txt'
curr=-1;
while 1:
    if b == False:
        state = 0; #无网络连接
    elif b==True&a==False:
        state = 1;#有内网连接
    else:
        state = 2;#有外网连接
    if curr==state:
        continue
        time.sleep(1)
    curr=state
    time.sleep(1)#每1s检查一次
    dt=datetime.now()
    string=str(dt.year)+' '+str(dt.month)+' '+str(dt.day)+' '+str(dt.hour)+' '+str(dt.minute)+' '+str(dt.second)+' '+str(state)
    with open(file_name, 'a') as file_obj:
        file_obj.write(string+'\n')
        print(string)