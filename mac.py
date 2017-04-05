#!usr/bin/env python3
#coding=utf-8  
import psutil
import json
#获取网卡名称和其ip地址，不包括回环  
def get_netcard():
    #定义一个组
    netcard_info = []
    info = psutil.net_if_addrs()
    for k,v in info.items():
        for item in v:
            #if item[0] == 2 and not item[1]=='127.0.0.1':
                netcard_info.append((k,item))
    return netcard_info
if __name__ == '__main__':  
    print (get_netcard())
    netcard_info = get_netcard()
    for k,item in netcard_info:
        print (k)
        print (item[0])
        print (item[0]==2)
        print (item[1])
        print (item[1]=='127.0.0.1')
        print ("----------------------")
        print (dir(item))
        print (dir(item[0]))
        print (type(item[0]))
        print (type(item.family))
        print ("#####################")
    print (len(netcard_info))
    #print (json.dumps(netcard_info)
