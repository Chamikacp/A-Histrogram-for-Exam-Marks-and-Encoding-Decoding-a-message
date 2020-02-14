prompt = input("Enter a text:")
rotation_integer = int(input("Enter a key in range of 1-25:"))
encoding = ''
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
for i in range(len(prompt)):
    cha = prompt[i]
    if cha in ALPHABET:
        current_i = ALPHABET.find(cha)
        new_i = (current_i + rotation_integer)%26
        new_cha = ALPHABET[new_i]
        encoding = encoding + new_cha
    else:
        encoding = encoding + cha
print("Encryption =",encoding)    


 
