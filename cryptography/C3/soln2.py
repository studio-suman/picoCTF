with open('orginal.py') as f:
    ciphertext = f.read()
asciichars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmn"
b = 1
for i in range(len(ciphertext)):
    if i == b*b*b:
        print(ciphertext[i])
        b += 1