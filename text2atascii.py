import os
import sys
def char_to_atachar(x):
    
    conv = {
        chr(0x2665): b'\x00', # kier
        chr(0x2660): b'\x7b', # pik
        chr(0x2666): b'\x60', # karo
        chr(0x2663): b'\x10', #trefle
        chr(0x2523): b'\x02', # ┣
        chr(0x2595): b'\x03', # ▕
        
    }
    if x.isascii():
        return bytes(x, 'ascii')
    else:
        return conv[x]
    
def convert(filein, fileout):
    # fileout must be open in binary mode
    for line in filein:
        decode_tab = []
        line = line.rstrip(os.linesep)
        print(line)
        for char in line:
            decode_tab.append(char_to_atachar(char))
        decode_tab.append(b'\x9b')
        print(decode_tab)
        decode_line = b''.join(decode_tab)
        fileout.write(decode_line)


if __name__ == "__main__":
    name_in = sys.argv[1]
    name_out = sys.argv[2]
    with open(name_in, "r") as filein:
        with open(name_out, "wb") as fileout:
            convert(filein, fileout)
