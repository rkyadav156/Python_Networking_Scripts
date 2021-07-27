# Very First we have to import the netmiko module
from netmiko import ConnectHandler

# We have to use dictionary datatype to create an objectof the router device
my_router={
    'device_type':'cisco_ios',
    'ip':'10.240.154.120',
    'username':'myid',
    'password':'mypass'
}

# After this we will create a connection 

net_con=ConnectHandler(**my_router)

# Now we have to get the hostname from the prompt
hostname = net_con.send_command('show run | i host')
hostname.split(" ")
hostname,device = hostname.split(" ")
print("Device is Backing Up"+ device)

# Assign a path to  save the backed up data
filename =  device + 'txt'

showrun = net_con.send_command('show run')
showvlan = net_con.send_command('show vlan')
showver =  net_con.semd_command('show ver')

# Open file in append mode to write the backup data
logfile = open(filename,"a")

logfile.write(showrun)
logfile.write("\n")
logfile.write(showvlan)
logfile.write("\n")
logfile.write(showver)
logfile.write("\n")

# Finally at the end close the connection

net_con.disconnect()