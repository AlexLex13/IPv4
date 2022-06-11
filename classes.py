class IPAdress:
    @classmethod
    def class_type(cls, bin_mask):
        if bin_mask[0][0] == '0':
            return 8

        elif bin_mask[0][:2] == '10':
            return 16

        elif bin_mask[0][:3] == '110':
            return 24

        elif bin_mask[0][:4] == '1110':
            return -1

        elif bin_mask[0][:5] == '11110':
            return -2

    def __init__(self, adr):
        self.str_adr = adr
        self.split_mask = adr.split('.')
        print(self.split_mask)
        self.bin_split_mask = [str(bin(int(octet)))[2:].zfill(8) for octet in self.split_mask]
        print(self.bin_split_mask)
        self.subnet_class = IPAdress.class_type(self.bin_split_mask)

    def __str__(self):
        if self.subnet_class == 8:
            return """Network class - A
                Subnet mask - 255.0.0.0
                Starting address - 1.0.0.0\tEnd address - 126.255.255.255
                Number of possible subnets - 126\tNumber of possible hosts - 16 777 214\n"""

        elif self.subnet_class == 16:
            return """Network class - B
                Subnet mask - 255.255.0.0
                Starting address - 128.0.0.0\tEnd address - 191.255.255.255
                Number of possible subnets - 16 384\tNumber of possible hosts - 65 534\n"""

        elif self.subnet_class == 24:
            return """Network class - C
                    Subnet mask - 255.255.255.0
                    Starting address - 192.0.0.0\tEnd address - 223.255.255.255
                    Number of possible subnets - 2 097 152\tNumber of possible hosts - 254\n"""

        elif self.subnet_class == -1:
            return """Network class - D
                    Group addresses
                    Starting address - 224.0.0.0\tEnd address - 239.255.255.255\n"""

        elif self.subnet_class == -2:
            return """Network class - E
                    Reserved addresses
                    Starting address - 240.0.0.0\tEnd address - 225.255.255.255\n"""


