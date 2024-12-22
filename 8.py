def decrypt_or_encrypt(original_text, shifted_position,dirn):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
                'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    changed_text =''
    if dirn == 'decode':
        shifted_position *= -1
    for letter in original_text :



         if letter in alphabet:
             shifted_number = alphabet.index(letter)+shifted_position
             shifted_number %= len(alphabet)
             changed_text+= alphabet[shifted_number]
         else:
            changed_text += letter
    print(changed_text)



again = True

while again :

    direction = input("Type encode to encrypt , type'decode' to  decrypt\n ")
    text = input("Type your message :\n").lower()
    shift = int(input("type the shift number \n"))
    decrypt_or_encrypt(text,shift,direction)
    yes_or_no = input("do you want to continue : 'yes' or 'no' ")
    if yes_or_no == 'no':
        again = False









