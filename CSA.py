
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
