# for termux
import os, json, sys

info = os.popen('ip addr').read()
ipv6_addr = info.split('wlan0')[-1].split('scope global temporary dynamic')[0].split('inet6')[-1].split('/')[0].strip()
ipv4_inner_addr = info.split('scope global wlan0')[0].split('inet')[-1].split('/')[0].strip()

data = {}
prefix = str(sys.argv[1])
data[prefix] = ipv6_addr
#data['ywz3in'] = ipv4_inner_addr

with open('myip.json', 'w') as f:
    json.dump(data, f)

print(data)
print('done')
os.system("timeout 3s ping6 {}.buaamc2.net".format(prefix))
