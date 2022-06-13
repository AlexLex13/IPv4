from classes import IPAdress

print('Programm start!')
ch = 'y'
while ch != 'n':
    mask = input("Enter the network in the given format {X.X.X.X}: ")
    number_of_networks = int(input("Enter number of subnets: "))
    number_of_hosts = int(input("Enter number of hosts: "))
    net = IPAdress(mask, number_of_networks, number_of_hosts)
    print(net.info())

    print(net.get_subnet_mask())

    choise = 'y'
    while choise != 'n':
        concrete_network, concrete_host = int(input("Enter a specific subnet: ")), int(input("Enter a specific host: "))
        print(net.concrete_adress(concrete_network, concrete_host))

        choise = input("Do you want to count another address? (y/n) : ")

    ch = input("Do you want to enter another network? (y/n) : ")
else:
    print('The programm is completed!')