#TODO refactor code and split up into multiple classes: 
# move to front; Huffman; CSA; and Burrows Wheeler from CSA import CSA
from time import clock
from CSA import CSA
class BWT():
    def encode(self,text):
        c = CSA(text)
        print(c)
        t=''
        for i in range(0,len(text)):
            index = c.getIndex(i)
            if index !=0:
                t+=text[c.getIndex(i)-1]
            else:
                t =str(i)+t
                t+=text[-1]
        print(t)
text = open('tests/6mb_test.txt','rb').read()

t= clock()
c = CSA(text)
print(clock()-t)
