import sys

def convert_cidr_to_subnet(cidr):
    subnet_bin = ''
    subnet = []
    for i in range(int(cidr)):
        subnet_bin += '1'
    while(len(subnet_bin)<32):
        subnet_bin += '0'
    for i in range(0, 32, 8):
        subnet.append(str(int(subnet_bin[i : i+8],2)))
    subnet_mask = '.'.join(subnet)
    return subnet_mask


def convert_subnet_to_cidr(subnet):
    subnet = subnet.split('.')
    for i in range(len(subnet)):
        subnet[i] = bin(int(subnet[i]))[2:].zfill(8)
    cidr = ''.join(subnet).count('1')
    return cidr


def calculate_network_address(ip, subnet):
    ip = ip.split('.')
    subnet = subnet.split('.')
    network = []
    for i in range(len(ip)):
        network.append(str(int(ip[i]) & int(subnet[i])))
    network = '.'.join(network)
    return network


def calculate_number_of_hosts(cidr):
    return 2**(32-int(cidr)) - 2


def calculate_broadcast_address(ip, cidr):
    host_bit = ''
    for i in range(32 - int(cidr)):
        host_bit += '1'
    host_bit = host_bit.zfill(32)
    ip_list = ip.split('.')
    host_mask = []
    for i in range(0, 32, 8):
        host_mask.append(str(int(host_bit[i : i+8],2)))
    broadcast = []
    for i in range(4):
        broadcast.append(str(int(ip_list[i]) or int(host_mask[i])))
    return '.'.join(broadcast)

ip_address = '' # i.e. 192.168.0.10
cidr = '' # i.e. 24
network_cidr = '' # i.e. 192.168.0.0/24
subnet_mask = '' # i.e. 255.255.255.0
network_address = '' # i.e. 192.168.0.0
broadcast_address = '' # i.e. 192.168.0.255

ip_address = sys.argv[1]
ip_address = ip_address.split('/')

if len(ip_address) > 1:
    cidr = ip_address[1]
    subnet_mask = convert_cidr_to_subnet(cidr)    
ip_address = ip_address[0]


if len(sys.argv) > 2:
    subnet_mask = sys.argv[2]
    cidr = convert_subnet_to_cidr(subnet_mask)

# calculate some stuff
network_address = calculate_network_address(ip_address, subnet_mask)
network_cidr = network_address + '/' + str(cidr)
print('IP address: ' + ip_address)
print('Network address: ' + network_address)
print('Subnet mask: ' + subnet_mask)
print('CIDR notation: ' + network_cidr)
print('Broadcast address: ' + calculate_broadcast_address(network_address, cidr))
print('Number of hosts: ' + str(calculate_number_of_hosts(cidr)))