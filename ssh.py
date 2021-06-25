from netmiko import ConnectHandler
 
cisco = {
    'ip': '10.1.1.1',
    'username': 'user',
    'password': 'P@ssword'
}
 
net_connect = ConnectHandler(**cisco)
 
output = net_connect.send_command('show run')
print (output)
 
net_connect.disconnect()
