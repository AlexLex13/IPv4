import IPv4
import os

print('Program start!')
ch = 'y'
while ch != 'n':
    os.system('CLS')
    mask = input("Enter the network in the given format X.X.X.X: ")
    number_of_networks, number_of_hosts = input("Enter number of subnets: "), \
                                          input("Enter number of hosts: ")

    try:
        net = IPv4.IPAdress(mask, int(number_of_networks), int(number_of_hosts))
    except ValueError:
        print(f'Number_of_networks and number_of_hosts must be numbers!')
    except IPv4.WrongFormat as WF:
        print(WF)
    except IPv4.SpecialAdress as SA:
        print(SA)
    except IPv4.NetworkNotExist as NNE:
        print(NNE)
    else:
        print(net.info())
        print(net.subnet_mask())

        choise = 'y'
        while choise != 'n':
            try:
                concrete_network, concrete_host = int(input("Enter a concrete subnet: ")), \
                                                  int(input("Enter a concrete host: "))
                if concrete_network > int(number_of_networks) or concrete_host > int(number_of_hosts):
                    raise IPv4.WrongNumber

                print(net.concrete_adress(concrete_network, concrete_host))

            except ValueError:
                print(f'Concrete_subnet and concrete_host must be numbers!')
            except IPv4.WrongNumber as WN:
                print(WN)

            choise = input("Do you want to count another address? (y/n) : ")

    ch = input("Do you want to enter another network? (y/n) : ")
else:
    print('The programm is completed!')
