#!/usr/bin/env python
# coding: utf-8

# In[10]:


import socket
# pip install ping3
import ping3

domain_list = ['github.global.ssl.fastly.net',
'github.com',
'assets-cdn.github.com',
'documentcloud.github.com',
'gist.github.com',
'cloud.githubusercontent.com',
'gist.githubusercontent.com',
'help.github.com',
'nodeload.github.com',
'codeload.github.com',
'status.github.com',
'training.github.com',
'avatars0.githubusercontent.com',
'avatars1.githubusercontent.com',
'avatars2.githubusercontent.com',
'avatars3.githubusercontent.com',
'avatars3.githubusercontent.com',
'avatars4.githubusercontent.com',
'avatars5.githubusercontent.com',
'avatars6.githubusercontent.com',
'avatars7.githubusercontent.com',
'avatars8.githubusercontent.com',
'avatars9.githubusercontent.com']



# 获取域名解析出的IP列表
def get_ip_list(domain): 
  ip_list = set()
  try:
    addrs = socket.getaddrinfo(domain, None)
    for item in addrs:
      ip_list.add(item[4][0])
  except Exception as e:
    pass
  return ip_list

def caclulate_fastest_ip():
    result = {}
    for domain in domain_list:
        ips = get_ip_list(domain)
        shortest_time = 10000
        for ip in ips:
            #print(ip, ' ', domain)
            cost_time = ping3.ping(ip, timeout = 1,unit = 'ms')
            if cost_time and cost_time < shortest_time:
                result[domain] = ip
                print(domain, ":", ip, ",time:", cost_time, "ms")
    return result

def generate_hosts_data():
    print("开始计算到可访问节点的速度:")
    ip_domain_dict = caclulate_fastest_ip()
    print("添加以下内容到/etc/hosts 来加速访问github.com")
    print('======================================')
    
    for ip_domain in ip_domain_dict:
        print(ip_domain_dict[ip_domain], ' ', ip_domain)
    print('======================================')
    append_hosts = input("输入y或yes将自动追加：")
    if append_hosts == 'y' or append_hosts == 'yes':
        try:
            f = open("/etc/hosts", "a+")
            for ip_domain in ip_domain_dict:
                f.write(ip_domain_dict[ip_domain],' ' ,ip_domain) 
            f.close()
        except Exception as e:
            print("写入失败:", e)
#print(get_ip_list('https://github.com/'))          
generate_hosts_data()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




