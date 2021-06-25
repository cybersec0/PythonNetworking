from netmiko import ConnectHandler

with open('devices') as devices:
    for iplist in devices:
        device = {
            'ip': iplist,
            'username': 'user',
            'password': 'P@ssword'
        }

        net_connect = ConnectHandler(**device)

        hostname = net_connect.send_command('show run | i host')
        hostname.split(" ")
        hostname,dev = hostname.split(" ")
        print (" " + dev)

        filename = '/home/user/devices/backup/' + device + '.txt'

        showrun = net_connect.send_command('show run')
        showvlan = net_connect.send_command('show vlan')
        showver = net_connect.send_command('show ver')
        log_file = open(filename, "a") 
        log_file.write(showrun)
        log_file.write("\n")
        log_file.write(showvlan)
        log_file.write("\n")
        log_file.write(showver)
        log_file.write("\n")
net_connect.disconnect()
