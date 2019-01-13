# TODO refactor code and split up into multiple classes: 
# move to front; Huffman; CSA; and Burrows Wheeler from CSA import CSA
from time import clock
from CSA import CSA
from Huffmant import Huffman
from MTF import moveToFront 
import sys, os.path, pickle,struct
from argparse import  ArgumentParser
from bitarray import bitarray

class BWT():
    def encode(self, text):
        c = CSA(text)
        t = bytearray()
        for i in range(0, len(text)):
            index = c.getIndex(i)
            if index != 0:
                t.append(text[c.getIndex(i) - 1])
            else:
                i_bytes = bytearray(i.to_bytes(4,byteorder = 'little', signed = False))
                t = i_bytes + t
                t.append(text[-1])
        return t
    
    def decode(self, t):
        # TODO write this function and make it work
        start_index, text, next, t = int.from_bytes(t[:4], byteorder = 'little', signed=False), bytearray(), [], t[4:]
        first = sorted(t)
        marked = [False] * len(first)
 
        for c in first:
            index = t.index(c)
            while marked[index]:
                index += t[index + 1:].index(c) + 1
            marked[index] = True
            next.append(index)
            
        for  i in range(0, len(next)):
            text.append(first[start_index])
            start_index = next[start_index]
        return text

b = BWT()
h = Huffman()

def BWT_encode(filename):
    startTime = clock()
    text = open(filename, 'rb+').read()
    text = h.compress(text)
    
    print('File compressed in ' + str(clock() - startTime) + ' seconds.')
    
parser = ArgumentParser(description="Burrows-Wheeeler-Compression")
parser.add_argument("--compress", help="filename")
parser.add_argument("--extract", help="filename")
args = parser.parse_args()
if args.compress:
    BWT_encode(args.compress)
elif args.extract:
    BWT_encode(args.extract)

