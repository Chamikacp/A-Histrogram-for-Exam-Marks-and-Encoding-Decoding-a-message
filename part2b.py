print("### SELECT THE COMMAND ###")
print("\nEnter 'e' to Encode the text.")
print("\nEnter 'd' to Decode the text.")
print("\nEnter 'q' to Quit." )

while True:
    
    select = input("\nEnter your command:")
    
    #To get the correct input
    if select == 'e':
        prompt = input("Enter a text:")
        
        #To get the correct integer value 1-25
        while True:
            rotation_integer = int(input("Enter a key in range of 1-25:"))
            
            if rotation_integer > 0 and rotation_integer < 26:
                encoding = ''
                ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
                
                for i in range(len(prompt)):
                    cha = prompt[i]

                    #To encode the string
                    if cha in ALPHABET:
                        current_i = ALPHABET.find(cha)
                        new_i = (current_i + rotation_integer) % 26
                        new_cha = ALPHABET[new_i]
                        encoding = encoding + new_cha

                    #If user has entered a upper case or etc    
                    else:
                        encoding = encoding + cha
                print("Encryption =",encoding)        
                break    
            
            else:
                print("Enter a number 1 to 25")
                
    elif select == 'd':
         prompt = input("Enter a text:")
         
         #To get the correct integer value 1-25
         while True:
             rotation_integer = int(input("Enter a key in range of 1-25:"))
             
             if rotation_integer > 0 and rotation_integer < 26:
                decoding = ''
                ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
                
                for i in range(len(prompt)):
                    cha = prompt[i]

                    #To decode the string
                    if cha in ALPHABET:
                        current_i = ALPHABET.find(cha)
                        new_i = (current_i - rotation_integer) % 26
                        new_cha = ALPHABET[new_i]
                        decoding = decoding + new_cha

                    #If user has entered a upper case or etc   
                    else:
                         decoding = decoding + cha
                print('Decryption = ',decoding)
                break
            
             else:
                print("Enter a number 1 to 25")
                
    elif select == 'q':
        break
    
    else:
        print("\nWrong command,Please enter a valid command.")
        
print("\nTHE END")        
