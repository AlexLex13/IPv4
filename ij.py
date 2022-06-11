def get_bin_subnet_mask(count_z_bits: int):

    number_of_networks = int(input("Enter number of subnets: "))
    number_of_hosts = int(input("Enter number of hosts: "))

    subnet_bits, bits_for_host = len(bin(number_of_networks)[2:]), len(bin(number_of_hosts)[2:])
    print(subnet_bits, bits_for_host)

    if subnet_bits + bits_for_host <= count_z_bits:
        print(f"255.255.{int('1' * subnet_bits, 2) << (8 - subnet_bits)}.0")
        return subnet_bits, bits_for_host

    else:
        return -1

