	
def make256():
    arr = bytearray()
    for i in range(0, 256):
        arr.append(i) 
    return arr

class moveToFront:
    def moveToFrontEn(self,text):
        out,alphabet= [],make256()
        for c in text:
            index = alphabet.index(c)
            out.append(index)
            alphabet_temp = bytearray()

            alphabet_temp.append(alphabet[index])
            alphabet = alphabet_temp+ alphabet[:index] + alphabet[index + 1:]
        return out
    
    def moveToFrontDe(self,out):
        text,alphabet = '',make256()
        for index in out:
            text += alphabet[index]
            alphabet = alphabet[index] + alphabet[:index] + alphabet[index + 1:]
        return text
    
