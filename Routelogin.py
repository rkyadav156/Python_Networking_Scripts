# First we need to import netmiko module by using pip install netmiko
from netmiko import ConnectHandler
import netmiko

# Take the sheet of router device 
with open('devices.txt') as routers :
    for IP  in routers:
        Router_Desc= {
            'device_type': 'cisco_ios',
            'ip':IP,
            'username':'myuserid',
            'password':'myuserpass'
        }

# Now create the connection to the devices
        net_con = ConnectHandler(**Router_Desc)
        print('Connecting To' + IP)
        print('_',*79)

# Save the output as below
        output = net_con.send_command('sh ip inf brief')
        print(output)
        print()
        print('_', *79)

# Now at the end just close the connection
net_con.disconnect()