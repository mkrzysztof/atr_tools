import sys

class ATRImage():
    def read_image(self, file_name):
        with open(file_name, mode='rb') as f:
            data = f.read()
            self.header = bytearray(data[0:0+16])
            self.image = bytearray(data[16:])

    def read_sectors(self, begin, end):
        sector_size = (self.header[5] << 8) + self.header[4]
        sectors = []
        for i in range(begin, end):
            sector = self.image[i*sector_size:i*sector_size + sector_size]
            sectors.append(sector)
        return sectors
    
    def read_dir_from_sector(self, sector):
        length_of_file_desc = 0x10
        directory = []
        for i in range(8):
            dir_node = sector[i*0x10:i*0x10+0x10]
            if dir_node[0] not in (0, 0x80):
                name = dir_node[5:5+11].decode()
                directory.append(name)
        return directory

    def read_directory(self):
        dir_sectors = self.read_sectors(0x168, 0x170)
        directory = []
        for sector in dir_sectors:
            dir_sector = self.read_dir_from_sector(sector)
            if dir_sector:
                directory.extend(dir_sector)
        return directory

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('Podaj plik atr w wywołaniu')
    else:
        file_name = sys.argv[1]
        atr_image = ATRImage()
        atr_image.read_image(file_name)
        directory = atr_image.read_directory()
        for d in directory:
            print(d)
