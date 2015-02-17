def make256():
    arr = bytearray()
    for i in range(0, 256):
        arr.append(i) 
    return arr

def moveToFront(self,text):
    out,alphabet= [],make256()
    for c in text:
        index = alphabet.index(c)
        out.append(index)
        alphabet_temp = bytearray()
        alphabet_temp.append(alphabet[index])
        alphabet = alphabet_temp+ alphabet[:index] + alphabet[index + 1:]
    return out

