#!/usr/bin/env python3

# 转为qx的proxy-list  direct-list 以及ad-list

import sys


# 读取  ./publish/direct-list.txt 
with open("./publish/direct-list.txt", 'r') as f:
    direct_list = f.readlines()
    
# 读取  ./publish/proxy-list.txt 
with open("./publish/proxy-list.txt", 'r') as f:
    proxy_list = f.readlines()
    
# 读取  ./publish/reject-list.txt
with open("./publish/reject-list.txt", 'r') as f:
    reject_list = f.readlines()

for proxy in proxy_list:
    print(proxy.strip())