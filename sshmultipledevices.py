from netmiko import ConnectHandler
#create file named devices on same directory with list of ip address.
with open('devices') as devices:
    for iprange in devices:
        device = {
            'ip': iprange,
            'username': 'user',
            'password': 'P@ssword'
        }

        net_connect = ConnectHandler(**device)

        print ('Configuring ' + iprange)
        print('*'*20)
        output = net_connect.send_command('sh run')
        print(output)
        print()
        print('*'*20)
net_connect.disconnect()
