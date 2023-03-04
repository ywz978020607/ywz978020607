# for termux
import os, json, sys

info = os.popen('ip addr').read()
ipv6_addr = '24' + info.split('inet6 24')[1].split('scope global')[0].split('/')[0].strip()
#ipv4_inner_addr = info.split('scope global wlan0')[0].split('inet')[-1].split('/')[0].strip()

data = {}
prefix = str(sys.argv[1])
data[prefix] = ipv6_addr
#data['ywz3in'] = ipv4_inner_addr

with open('myip.json', 'w') as f:
    json.dump(data, f)

print(data)
print('done')
os.system("timeout 3s ping6 {}.buaamc2.net".format(prefix))
