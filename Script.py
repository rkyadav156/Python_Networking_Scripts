from netmiko import ConnectHandler

with open('commands_file') as f:
    commands_list = f.read().splitlines()

with open('devices_file') as f:
    devices_list = f.read().splitlines()

for devices in devices_list:
    print ('Connecting to device" ' + devices)
    ip_address_of_device = devices_list
    ios_device = {
        'device_type': 'cisco_ios',
        'ip': 'ip_address_of_device',
        'username': '',
        'password': '',
        'secret': ''
    }
net_connect = ConnectHandler(**ios_device)
output = net_connect.send_config_set(commands_list)
print (output)

net_connect = ConnectHandler(**ios_device)
output = net_connect.send_command_expect('test aaa group tacacs+ readonly Temp1234 legacy')
print (output)