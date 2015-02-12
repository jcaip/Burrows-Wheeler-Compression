	
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
