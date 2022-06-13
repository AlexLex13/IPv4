class IPAdress:

    def __init__(self, adr, number_of_networks, number_of_hosts):
        self.adr = adr
        self.net_class, self.net_mask = self.__class_type(self.dec_to_bin(self.adr))
        self.verify_mask(len(bin(number_of_networks)[2:]), len(bin(number_of_hosts)[2:]), self.net_class)
        self.subnet_bits, self.bits_for_host = len(bin(number_of_networks)[2:]), len(bin(number_of_hosts)[2:])

    @classmethod
    def verify_adr(cls, fio):
        pass

    @classmethod
    def verify_mask(cls, subnet_bits, bits_for_host, net_class):
        if subnet_bits + bits_for_host > net_class:
            raise NetworkNotExist

    @classmethod
    def __class_type(cls, binmsk):
        bin_mask = binmsk.split('.')
        if bin_mask[0][0] == '0':
            return 24, '255.0.0.0'

        elif bin_mask[0][:2] == '10':
            return 16, '255.255.0.0'

        elif bin_mask[0][:3] == '110':
            return 8, '255.255.255.0'

        elif bin_mask[0][:4] == '1110':
            raise SpecialAdress

        elif bin_mask[0][:5] == '11110':
            raise SpecialAdress

    @classmethod
    def dec_to_bin(cls, adr):
        return '.'.join([str(bin(int(octet)))[2:].zfill(8) for octet in adr.split('.')])

    @classmethod
    def bin_to_dec(cls, adr):
        return '.'.join([str(int(octet, 2)) for octet in adr.split('.')])

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

    def get_subnet_mask(self):

        bin_subnet_mask = ''.join(self.dec_to_bin(self.net_mask).split('.')[:int((32 - self.net_class) / 8)]) + \
                          '1' * self.subnet_bits + '0' * (self.net_class - self.subnet_bits)
        return self.bin_to_dec('.'.join(list(map(''.join, zip(*[iter(bin_subnet_mask)] * 8)))))

    def concrete_adress(self, concrete_network, concrete_host):
        result = ''.join(self.dec_to_bin(self.adr).split('.')[:int((32 - self.net_class) / 8)]) + \
                 bin(concrete_network)[2:].zfill(self.subnet_bits) + \
                 bin(concrete_host)[2:].zfill(self.net_class - self.subnet_bits)
        return self.bin_to_dec('.'.join(list(map(''.join, zip(*[iter(result)] * 8)))))

    def __str__(self):
        return self.adr

    @property
    def adr(self):
        return self.__adr

    @adr.setter
    def adr(self, adr):
        self.verify_adr(adr)
        self.__adr = adr

    @property
    def net_class(self):
        return self.__net_class

    @net_class.setter
    def net_class(self, net_class):
        self.__net_class = net_class

    @property
    def net_mask(self):
        return self.__net_mask

    @net_mask.setter
    def net_mask(self, net_mask):
        self.__net_mask = net_mask

    @property
    def subnet_bits(self):
        return self.__subnet_bits

    @subnet_bits.setter
    def subnet_bits(self, subnet_bits):
        self.__subnet_bits = subnet_bits

    @property
    def bits_for_host(self):
        return self.__bits_for_host

    @bits_for_host.setter
    def bits_for_host(self, bits_for_host):
        self.__bits_for_host = bits_for_host


class NetworkNotExist(Exception):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return 'NetworkNotExist'


class SpecialAdress(Exception):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return 'SpecialAdress'
