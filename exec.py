from classes import IPAdress, sum_mask

mask = input("Enter the network in the given format {X.X.X.X}: ")
net = IPAdress(mask)
network = sum_mask(net.str_adr, net.net_mask)
print(network, net.info())

number_of_networks = int(input("Enter number of subnets: "))
number_of_hosts = int(input("Enter number of hosts: "))

subnet_mask = net.get_subnet_mask(number_of_networks, number_of_hosts)
print(subnet_mask)
print(sum_mask(net.str_adr, subnet_mask))

# choise = 'y'
# while choise != 'n':
#     concrete_network, concrete_host = int(input("Enter a specific subnet: ")), int(input("Enter a specific host: "))
#     print()
#
#     choise = input("Do you want to count another address? (y/n) : ")
