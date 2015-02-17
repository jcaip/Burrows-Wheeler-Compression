#TODO refactor code and split up into multiple classes: 
# move to front; Huffman; CSA; and Burrows Wheeler from CSA import CSA
from time import clock
from CSA import CSA
from Huffmant import Huffman
from MTF import moveToFront 
import sys

class BWT():
    def encode(self,text):
        c = CSA(text)
        t=bytearray()
        for i in range(0,len(text)):
            index = c.getIndex(i)
            if index !=0:
                t.append(text[c.getIndex(i)-1])
            else:
                i_bytes = bytearray((i).to_bytes(4, byteorder = sys.byteorder))
                t = i_bytes+t
                t.append(text[-1])
        return t
    
    def decode(self,t):
        #TODO write this function and make it work
        index = int.from_bytes(bytes(t[:4]), byteorder = sys.byteorder,signed=False)
        print(index)
        text = bytearray()
        next = []
        text.lstrip()
        first = sorted(t)
        for c in first:
            next.append(t.index(c))
        for index in next:
            text.append(t[index])
        return text

#testing code
t = clock()

b = BWT()
h = Huffman()

text = open('tests/6mb_test.txt','rb').read()

text_BWT = b.encode(text)
b.decode(text_BWT)
"""print(clock()-t)
text_MTF = m.moveToFrontEn(text_BWT)
print(clock()-t)
text_HUF = h.compress(text_MTF)
print(clock()-t)"""

f = open('output.enc','wb')
text_HUF.tofile(f)
f.close()
