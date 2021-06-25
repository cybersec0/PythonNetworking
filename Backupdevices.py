import getpass

import telnetlib

import time

from netmiko import ConnectHandler

time1=time.time()

Switch1 = {

    ‘device_type’: ‘cisco_ios’,

    ‘ip’: ‘10.1.1.1’,

    ‘username’: ‘user’,

    ‘password’: ‘P@ssword’, 

    ‘secret’ : ‘passw0rd’,

    ‘global_delay_factor’: 2,

 }

Switch2 = {

    ‘device_type’: ‘cisco_ios’,

    ‘ip’: ‘10.1.1.2’,

    ‘username’: ‘user’,

    ‘password’: ‘P@ssword’, 

    ‘secret’ : ‘passw0rd’,
  
    ‘global_delay_factor’: 2,

 }

Switch3 = {

    ‘device_type’: ‘cisco_ios’,

    ‘ip’: ‘10.1.1.3’,

    ‘username’: ‘user’,

    ‘password’: ‘P@ssword’, 

    ‘secret’ : ‘passw0rd’,

    ‘global_delay_factor’: 2,

 }

Switch4 = {

    ‘device_type’: ‘cisco_ios’,

    ‘ip’: ‘10.1.1.4’,

    ‘username’: ‘user’,

    ‘password’: ‘P@ssword’, 

    ‘secret’ : ‘passw0rd’,

    ‘global_delay_factor’: 2,

 }

router_list=[Switch1, Switch2, Switch3, Switch4]

name_list=[‘Switch1′,’Switch2′,’Switch3′,’Switch4’]

name_list1=[‘Switch1.txt’,’Switch2.txt’,’Switch3.txt’,’Switch4.txt’]

count=0

for device in router_list:

    net_connect = ConnectHandler(**device)

    out= net_connect.find_prompt()

    print(out)

    out1=str(out)

    out=net_connect.enable()

    out2= net_connect.find_prompt()

    print (“Collecting backup from device: ” +str(name_list[count]))

    #outp=net_connect.send_command(“terminal length 0”)

    net_connect.send_command(“en”)

    net_connect.send_command(“passw0rd”)

    output1 = net_connect.send_command(“show clock”,delay_factor=2)

    output2 = net_connect.send_command(“show run”,delay_factor=2)

    saveoutput=open((name_list1[count]),”w”)

    saveoutput.write(out2)

    saveoutput.write(‘show clock \n’)

    saveoutput.write(output1)

    saveoutput.write(‘\n\n’)

    saveoutput.write(out2)

    saveoutput.write(‘show run \n’)

    saveoutput.write(output2)

    saveoutput.write(‘\n’)

    saveoutput.write(out2)

    saveoutput.write(‘\n’)

    saveoutput.close()

    print (“Backup sucessfull for Device ” +str(name_list[count]))

    print (“\n”)

    count=count+1

time2=time.time()

print(“Total time taken for complete procedure : ” +str(time2-time1))

time.sleep(4)
