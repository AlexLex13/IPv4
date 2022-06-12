class IPAdress:

    @staticmethod
    def __class_type(binmsk):
        bin_mask = binmsk.split('.')
        if bin_mask[0][0] == '0':
            return 24, '255.0.0.0'

        elif bin_mask[0][:2] == '10':
            return 16, '255.255.0.0'

        elif bin_mask[0][:3] == '110':
            return 8, '255.255.255.0'

        elif bin_mask[0][:4] == '1110':
            return -1, '-1'

        elif bin_mask[0][:5] == '11110':
            return -2, '-2'

    @staticmethod
    def dec_to_bin(adr):
        return '.'.join([str(bin(int(octet)))[2:].zfill(8) for octet in adr.split('.')])

    def __init__(self, adr):
        self.str_adr = adr
        self.bin_split_mask = self.dec_to_bin(self.str_adr)
        self.net_class, self.net_mask = self.__class_type(self.bin_split_mask)

    def info(self):
        if self.net_class == 24:
            return """Network class - A
                Subnet mask - 255.0.0.0
                Starting address - 1.0.0.0\tEnd address - 126.255.255.255
                Number of possible subnets - 126\tNumber of possible hosts - 16 777 214\n"""

        elif self.net_class == 16:
            return """Network class - B
                Subnet mask - 255.255.0.0
                Starting address - 128.0.0.0\tEnd address - 191.255.255.255
                Number of possible subnets - 16 384\tNumber of possible hosts - 65 534\n"""

        elif self.net_class == 8:
            return """Network class - C
                    Subnet mask - 255.255.255.0
                    Starting address - 192.0.0.0\tEnd address - 223.255.255.255
                    Number of possible subnets - 2 097 152\tNumber of possible hosts - 254\n"""

        elif self.net_class == -1:
            return """Network class - D
                    Group addresses
                    Starting address - 224.0.0.0\tEnd address - 239.255.255.255\n"""

        elif self.net_class == -2:
            return """Network class - E
                    Reserved addresses
                    Starting address - 240.0.0.0\tEnd address - 225.255.255.255\n"""

    def get_subnet_mask(self, number_of_networks, number_of_hosts):

        subnet_bits, bits_for_host = len(bin(number_of_networks)[2:]), len(bin(number_of_hosts)[2:])
        print(subnet_bits, bits_for_host)

        if subnet_bits + bits_for_host <= self.net_class:
            return sum_mask(self.net_mask, self.str_adr)

        else:
            return -1

    def __str__(self):
        return self.str_adr


def sum_mask(this, other):
    this_list = this.split('.')
    other_list = other.split('.')
    return '.'.join([str(int(this_list[i]) | int(other_list[i])) for i in range(4)])
