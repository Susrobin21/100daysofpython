alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
end_game = False
while end_game == False :
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    length = len(alphabet)
    if shift > 45 :
        shift = round(shift % 26)

    def encrypt(input_text, shift_number):
        cipher_text = ''
        for letter in input_text:
            index_value = alphabet.index(letter)
            new_value = index_value + shift_number
            new_text = alphabet[new_value]
            cipher_text += new_text
        print(f'the cipher text is {cipher_text}')

    def decrypt(input_text, shift_number):
        decode_text = ''
        for letter in input_text:
            index_value = alphabet.index(letter)
            new_value = index_value - shift_number
            new_text = alphabet[new_value]
            decode_text += new_text
        print(f'the decoded text is {decode_text}')
    if direction == 'encode':
        encrypt(text,shift)
    else :
        decrypt(text,shift)
    yesorno = input('Do you want to continue the game :')
    if yesorno == 'no' :
        end_game = True
        print('Goodbye !')
    else :
        end_game

