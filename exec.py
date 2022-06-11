from classes import IPAdress

mask = input("Enter the network in the given format {X.X.X.X}: ")
net = IPAdress(mask)
print(net)

# choise = 'y'
# while choise != 'n':
#     concrete_network, concrete_host = int(input("Enter a specific subnet: ")), int(input("Enter a specific host: "))
#     fg = str(bin(concrete_network)[2:]).zfill(subnet_bits - len(bin(concrete_network)[2:])) + \
#          str(bin(concrete_host)[2:]).zfill(bits_for_host - len(bin(concrete_host)[2:]))
#     print(fg)
#     print(f"{int(bin_split_mask[0], 2)}.{int(bin_split_mask[1], 2)}.{int(fg[0:8], 2)}.{int(fg[8:16], 2)}")
#
#     choise = input("Do you want to count another address? (y/n) : ")
