
import getpass
import telnetlib

HOST = "localhost"
user = input("Enter username: ")
password = getpass.getpass()

# Create a file named devices and add switches mangement ip addresses of switches
f = open ('devices')

for IP in f:
      IP = IP.strip()
    print (" Configuring..." + (IP))
    HOST = IP
    tn = telnetlib.Telnet(HOST)
    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\n") 
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")

    tn.write(b"enable\n")
    tn.write(b"P@ssword\n")
    tn.write(b"conf t\n")
    tn.write(b"vlan 2\n")
    tn.write(b"name Py_vlan2\n")
    tn.write(b"vlan 3\n")
    tn.write(b"name Py_vlan3\n")
    tn.write(b"vlan 4\n")
    tn.write(b"name Py_vlan4\n")
    tn.write(b"end\n")
    tn.write(b"exit\n")

    print(tn.read_all().decode('ascii'))
