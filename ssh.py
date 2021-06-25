from netmiko import ConnectHandler
 
CSR = {
    'ip': '10.1.1.1',
    'username': 'user',
    'password': 'P@ssword'
}
 
net_connect = ConnectHandler(**CSR)
 
output = net_connect.send_command('show ip int brief')
print (output)
 
net_connect.disconnect()
