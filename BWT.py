#TODO refactor code and split up into multiple classes: 
# move to front; Huffman; CSA; and Burrows Wheeler from CSA import CSA
from time import clock
from CSA import CSA
from Huffmant import Huffman
from MTF import moveToFront 
import sys,os.path
from argparse import  ArgumentParser

class BWT():
    def encode(self,text):
        c = CSA(text)
        print(c.index)
        t=bytearray()
        for i in range(0,len(text)):
            index = c.getIndex(i)
            if index !=0:
                t.append(text[c.getIndex(i)-1])
            else:
                i_bytes = bytearray((i).to_bytes(4, byteorder = sys.byteorder,signed = False))
                t = i_bytes+t
                t.append(text[-1])
        return t
    
    def decode(self,t):
        #TODO write this function and make it work
        start_index, text, next,t = int.from_bytes(bytes(t[:4]), byteorder = sys.byteorder,signed=False), bytearray(), [],t[4:]
        first = sorted(t)
        marked = [False]*len(first)
 
        for c in first:
            index = t.index(c)
            while marked[index]:
                index+=t[index+1:].index(c)+1
            marked[index] = True
            next.append(index)
            
        for  i in range(0,len(next)):
            text.append(first[start_index])
            start_index = next[start_index]
        return text

#testing code
def is_valid_file(parser, arg):
    if not os.path.exists(arg):
        parser.error("The file %s does not exist!" % arg)
    else:
        return open(arg, 'rb')  # return an open file handle


parser = ArgumentParser(description="Burrows-Wheeeler-Compression")
parser.add_argument("-c", dest="filename", required=True, help="compress",type=lambda x: is_valid_file(parser, x))
parser.add_argument("-x", dest="filename", required=True, help="extract",type=lambda x: is_valid_file(parser, x))
args = parser.parse_args()

b = BWT()
h = Huffman()

def BWT_encode(filename):
    text = open(filename,'rb').read()
    text = b.encode(text)
    text = moveToFront(text)
    text = h.compress(text)
    
def BWT_decode(filename):
    text = open(filename, 'rb').read()
    text = h.extract(text)
    text = moveToFront(text)
    text = b.decode(text)
    


