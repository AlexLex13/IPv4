import IPv4
import tkinter

print('Program start!')
ch = 'y'
while ch != 'n':
    mask = input("Enter the network in the given format X.X.X.X: ")
    try:
        number_of_networks, number_of_hosts = int(input("Enter number of subnets: ")), \
                                              int(input("Enter number of hosts: "))
    except ValueError:
        print(f'number_of_networks, number_of_hosts -> str')
    else:

        try:
            net = IPv4.IPAdress(mask, number_of_networks, number_of_hosts)
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
                    concrete_network, concrete_host = int(input("Enter a specific subnet: ")), \
                                                    int(input("Enter a specific host: "))
                except ValueError:
                    print(f'number_of_networks, number_of_hosts -> str')
                else:
                    print(net.concrete_adress(concrete_network, concrete_host))

                choise = input("Do you want to count another address? (y/n) : ")

    ch = input("Do you want to enter another network? (y/n) : ")
else:
    print('The programm is completed!')
