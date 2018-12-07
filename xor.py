import base64
highscore = int()
plaintext = str()
ciphertext = "L0EFFQgPE1QEBFIADgRSAgMTC1QEBAEAbC0bHwNBHBtGDhwRRgQEERRBBRUVayYbRgITAAUJUgAOBB9UDxJSGR9BABEHDVIAAxIGfjIOUgAUABsaRhUaEQtBGwdGDAtUBQAHBwNreD1GFhsYCkEGBgcXFxhGABEGCRIBVBIJF1QKABwQbDIXFRQCGh0IBlISBxNSFQgFUgMPBRd+MgQTFw5BIhsNBB8bCEEGG0YUHBADEwEABw8WfjIJF1QWDgURFEEGHAcVVQdGCBwHDwUXfmwxHR8DDB0aR0E1GxIVE1QFAAYXDkFVEQtBExgKazsAQRJSDQkUUhUIBVIZA2s7VA0PHQNGCAZTFUEfDUYFFwcSCBwNbDEdHwMMHRpHQT0cSkELGxNGABFGDAtUBAQBAEYHAB0DDxZ+Lw9SFUYWHQYKBVIDA0EfARUVUhADBxcaAg=="
wordlist = open("words.txt", "r").read().split("\n")
    
def xorTest():
plaintext = input("Plaintext:")
key = input("Key:")
encrypted = ''
ptbuilder = ''
for i in range (len(plaintext)):
    key_i = i%len(key)
    print(chr(ord(plaintext[i])^ord(key[key_i])))
    encrypted = encrypted + chr(ord(plaintext[i])^ord(key[key_i]))
    
for i in range (len(encrypted)):
    key_i = i%len(key)
    print(chr(ord(encrypted[i])^ord(key[key_i])))
    ptbuilder = ptbuilder + chr(ord(plaintext[i])^ord(key[key_i]))

def xorFxn(text, key):
    result = str()
    for i in range(len(text)):
        text_decimal = ord(text)
        key_decimal = ord(key)
        new_decimal = text_decimal^key_decimal
        new_character = chr(new_decimal)
        result += new_character
    return result

def bruteXorce():
    global wordlist
    global ciphertext
    for word in wordlist:
        result = xor(ciphertext, word)
        print(result)

def score(text):
    global highscore
    global plaintext
    tmp = int()
    text = text.split()
    for word in text:
        if word in wordlist:
            tmp+=1
    if tmp > highschore:
        highscore = tmp
        plaintext = " ".join(text)
