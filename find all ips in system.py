import ifcfg
ip=[]
for name, interface in ifcfg.interfaces().items():
    if(interface['inet4']):
        ip.append(interface['inet4'][0])

print(ip)

for x in ip:
    if("10.0" in x):
        i__P = x
        print(x)


from requests import get

ip = get('https://api.ipify.org').text
print ('My public IP address is:', ip)