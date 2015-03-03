from functools import cmp_to_key
class CSA:
    def __init__(self, text):
        self.len = len(text)
        self.index = self.makeCSA(text)
        
    def makeCSA(self, text):

        def csaComp(i, j):
            while text[i] == text[j]:
                i = (i + 1) % len(text)
                j = (j + 1) % len(text)
            return text[i] - text[j]
            
        
        index = range(0, len(text))
        
        index = sorted(index, key=cmp_to_key(csaComp))
        return index

    def getLen(self):
        return self.len
    def getIndex(self, i):
        return self.index[i]
