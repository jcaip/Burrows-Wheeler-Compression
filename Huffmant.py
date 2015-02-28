from bitarray import bitarray
from heapq import heappop,heappush
from collections import defaultdict, deque

class Memoize:
    def __init__(self, f):
        self.f = f
        self.memo = {}
    def __call__(self, *args):
        if not args in self.memo:
            self.memo[args] = self.f(*args)
        return self.memo[args]

class Node:
    def __init__(self,l,r,c,v):
        self.left = l
        self.right = r
        self.char = c
        self.val = v
    def addVal(self,v):
        self.val.insert(0,v)#writes backwayrds- basically the bits that represent a character are flipped but not the order that they are arranged - its faster this way
        if self.left and self.right != None:
            self.right[1].addVal(v)#this is really wrong, but since this Node class is private, it is the easiest way to do it. Do not refactor 
            self.left[1].addVal(v)
        return 0
    def __lt__(self, n):
        return 0
        #this is not a real comparison - this is necessary when the counts of two characters are the same, the heapq then calls comparison on the node objects
        #because it is the next element in the tuple. at this point it does not matter what happens, either character can be taken from the list, so we return a value

    def __str__(self):
        return str(self.val)
    __repr__ = __str__

class Huffman:			
    def compress(self,text):
        def makeTree(text):
            d = defaultdict(int)
            for ch in text:
                d[ch]+=1
            pq = []
            vals = d.items()
            for i in vals:
                n = (i[1],Node(None ,None,i[0],bitarray()))
                heappush(pq,n)
            while len(pq)>1:
                n1,n2 = heappop(pq), heappop(pq)
                n1[1].addVal(False)
                n2[1].addVal(True)
                n = (n1[0]+n2[0],Node(n1,n2,None,bitarray()))
                heappush(pq,n)
            return pq[0]
            
        def huffPuff(char,htree):
            queue = deque([])
            queue.append(htree)
            while len(queue) > 0:
                t = queue.popleft()[1]
                if t.char ==char :
                    return t.val
                if t.left and t.right != None:
                    queue.append(t.left)
                    queue.append(t.right)

            return "String cannot be found" 
        
        hPF = Memoize(huffPuff)

        huffman = makeTree(text)
        comp = bitarray()
        for c in text:
            comp.extend(hPF(c,huffman))
        return (huffman,comp)

    def extract(self,tree,ctext):
        #TODO add method for getting tree for extraction function 
        val,i = bytearray(),0
        while i <ctext.length():
            huffTree = tree
            while huffTree[1].char == None:
                if ctext[i]:
                    huffTree = huffTree[1].right
                else:
                    huffTree= huffTree[1].left
                i+=1
            val.append(huffTree[1].char)
        return val



"""t= time.clock()
f = open('extract.txt','wb+')
xtext = h.extract(ctext[0],ctext[1])
print("Extraction finished. Time: ")
print(time.clock()-t)
f.write(xtext)
f.close"""

