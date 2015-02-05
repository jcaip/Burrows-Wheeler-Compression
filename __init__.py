from heapq import heapify,heappop,heappush
from collections import defaultdict

def make256():
    arr = b''
    for i in range(0, 256):
        arr += chr(i)
    return arr

class moveToFront:
    def moveToFrontEn(self,text):
        out,alphabet= [],make256()
        for c in text:
            index = alphabet.index(c)
            out.append(index)
            alphabet = alphabet[index] + alphabet[:index] + alphabet[index + 1:]
        return out
    
    def moveToFrontDe(self,out):
        text,alphabet = '',make256()
        for index in out:
            text += alphabet[index]
            alphabet = alphabet[index] + alphabet[:index] + alphabet[index + 1:]
        return text
    
    def __init__(self,data ,flag): 
        if(flag):
            self.out = self.moveToFrontEn(data)
        else:
            self.out = self.moveToFrontDe(data)
            
    def output(self):
        return self.out

class CSA:
    def __init__(self, text):
        self.len = len(text)
        self.index = self.makeCSA(text)
        
    def makeCSA(self,text):
        arr, index = [], range(0, len(text))
        for i in index:
            arr.append(text[i:] + text[:i])
        zipped = zip(index, arr)
        zipped.sort(key=lambda t: t[1])
        return list(zip(*zipped)[0])
    
    def getLen(self):
        return self.len
    def getIndex(self, i):
        return self.index[i]

def bwtransform(path):
	text = open(filename,'rb').read()
	c = CSA(text)
	
	

class Node:
		def __init__(self,l,r,p,c):
			self.left = l
			self.right = r
			self.prob = p
			self.char = c
		def __eq__(self,other):
			return self.prob==other.prob

class Huffman:			
	def compress(self,text):
		d = defaultdict(int)
		for ch in text:
			d[ch]+=1
		
		pq = []
		vals = d.items()
		
		for i in vals:
			n = Node(None ,None ,i[1],i[0])
			heappush(pq,n)
		
		while len(pq)>1:
			n1,n2 = heappop(pq), heappop(pq)
			p1,p2 = n1.prob,n2.prob
			n = Node(n1,n2,p1+p2,None)
			heappush(pq,n)
		
		hufftree = pq[0]
		for c in text:
		
		
		
		
	def extract(self,tree):
		
			
h = Huffman()
text = 'how are you doing today. attack at dawn lol little bitch'
print h.compress(text).prob
print len(text)



