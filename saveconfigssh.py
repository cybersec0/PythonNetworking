from netmiko import ConnectHandler
from getpass import getpass

username = input('Username: ')
password = getpass()

device = {
    'ip': '10.1.1.1',
    'username': 'user',
    'password': 'P@ssword'

}

net_connect = ConnectHandler(**device)

print('*'*20)
print('saving... ')
print('*'*20)

output = net_connect.save_config()
print(output)

print('*'*20)
print('Config Saved ')
print('*'*20)
