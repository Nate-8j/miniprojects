# f'{int(ip):032b}'
# bin(int(ip))[2:].zfill(32)



# from ipaddress import *
# net = ip_network('142.108.56.118/255.255.255.240', False)
# cnt = 0
# for ip in net:
#     s = bin(int(ip))[2:].zfill(32)
#     if s[:-16].count('1') < s[-16:].count('1'):
#         cnt += 1

# print(cnt)


# from ipaddress import *

# for m in range(16, 25):
#     net = ip_network(f'199.59.129.3/{m}', False)
#     res = []
#     for ip in net:
#         s = bin(int(ip))[2:].zfill(32)
#         res.append(s[:16].count('1') >= s[16:].count('1'))
#     if all(res):
#         print(net.netmask)

from ipaddress import ip_network
cnt = 0
for m in range(17, 25):
    net = ip_network(f'255.211.33.160/{m}', False)
    res = []
    for ip in net:
        s = f'{int(ip):032b}'
        res.append(s[:16].count('1') >= s[16:].count('1'))
    if all(res):
        cnt += 1
print(cnt)