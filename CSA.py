
class CSA:
    def __init__(self, text):
        self.len = len(text)
        self.index = self.makeCSA(text)
        
    def makeCSA(self,text):
        class csaIndex: #TODO switch python interperter to 2.7 and use cmp instead of thes bullshit

            def __init__(self,i):
                self.index = i

            def __lt__(self,other):
                i,j = self.index, other.index
                while text[i] ==text[j]:
                    i =(i+1)%len(text)
                    j = (j+1)%len(text)
                return (text[i] - text[j])<0
            
        
        index = [csaIndex(i) for i in range(0, len(text))]
        
        index = sorted(index)
        return [i.index for i in index]

    def getLen(self):
        return self.len
    def getIndex(self, i):
        return self.index[i]
