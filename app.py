from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import os

# CBC

def main():
    print("Escoge alguna opcion")
    print('1.- Encriptar mensaje')
    print('2.- Desencriptar mensaje')
    print('3.- Salir')

    value = int(input())
    os.system('clear')

    if value == 1:
        crypt()
    elif value == 2:
        decrypt()
    elif value == 3:
        exit()
    elif value != 1 or 2 or 3:
        print('Opcion incorrecta intenta nuevamente'), main()  

def crypt():

    key = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_CBC)

    message = b'Verse, an occasional synonym for poetry. Verse (poetry), a metrical structure, a stanza. Blank verse, a type of poetry having regular meter but no rhyme. Free verse, a type of poetry written without the use of strict meter or rhyme, but still recognized as poetry. Versed, 2009 collection of poetry by Rae Armantrout.'
    ciphertext = cipher.encrypt(pad(message, AES.block_size))

    with open('test.key','wb') as key_out:
        key_out.write(key)

    with open('cryptedFile','wb') as file_out:
        file_out.write(cipher.iv)
        file_out.write(ciphertext)

    print('Hash:', ciphertext, "\n")

    return main()
    
def decrypt():

    with open('cryptedFile','rb') as file_in:
        iv = file_in.read(16)
        ciphertext = file_in.read()

    with open('test.key','rb') as key_in:
        key = key_in.read()

    cipher = AES.new(key,AES.MODE_CBC, iv)
    pt = unpad(cipher.decrypt(ciphertext), AES.block_size)
    print('El mensaje es:', pt.decode(),"\n")
    
    return main()

def exit():
    return print('Bai')


main()