from netmiko import ConnectHandler 
import getpass

#########################################################
# FUNCTION:


def ntmk_jnpr(command):
    print(str(command))
    output = str(net_connect.send_command(command, expect_string=r"#|:"))  # It will get the command statement as argument and will be waiting on the strings # or :
   
    if output != '\n': # It will not print anything if there is no output from the command
        print(output)


#########################################################
# EXAMPLE HOW TO USE IT:

username = '<USERNAME>'
password = getpass.getpass()

net_connect = ConnectHandler(device_type='juniper_junos', ip='<IP_ADDRESS>', username=username, password=password, global_delay_factor=0.5)

ntmk_jnpr('show configuration | display set | match "node0 system host-name"')
