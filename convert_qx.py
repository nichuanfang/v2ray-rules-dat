#!/usr/bin/env python3

# 转为qx的proxy-list  direct-list 以及ad-list

qx_proxy_list = []
qx_reject_list = []

# 读取  ./publish/proxy-list.txt 
with open("./publish/proxy-list.txt", 'r') as f:
    proxy_list = f.readlines()
    
# 读取  ./publish/reject-list.txt
with open("./publish/reject-list.txt", 'r') as f:
    reject_list = f.readlines()

# 生成代理文件
for proxy in proxy_list:
    if proxy.strip().startswith('full:'):
        qx_proxy_list.append(f'HOST,{proxy.strip()}, PROXY')
    elif proxy.strip().startswith('regexp:'):
        continue
    else:
        qx_proxy_list.append(f'HOST-SUFFIX,{proxy.strip()}, PROXY')
        
# 生成拒绝文件
for reject in reject_list:
    if reject.strip().startswith('full:'):
        qx_reject_list.append(f'HOST,{reject.strip()}, REJECT')
    elif reject.strip().startswith('regexp:'):
        continue
    else:
        qx_reject_list.append(f'HOST-SUFFIX,{reject.strip()}, REJECT')
        
# 保存文件
with open("./publish/proxy-list.txt", 'w') as f:
    f.write('\n'.join(qx_proxy_list))
    
with open("./publish/reject-list.txt", 'w') as f:
    f.write('\n'.join(qx_reject_list))