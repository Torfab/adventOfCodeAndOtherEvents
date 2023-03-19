from PIL import Image
import binascii

img = Image.open("input.png", mode='r')

red, green, blue=img.split()

element=[]


for i in range(800):
  for j in range(1200):
    if(red.getpixel((j,i))%2==0):
      element.append('0')
    else:
      element.append('1')


def int2bytes(i):
    hex_string = '%x' % i
    n = len(hex_string)
    return binascii.unhexlify(hex_string.zfill(n + (n & 1)))

def text_from_bits(bits, encoding='utf-8', errors='surrogatepass'):
    n = int(bits, 2)
    return int2bytes(n).decode(encoding, errors)

b="".join(element)


print(text_from_bits(b))