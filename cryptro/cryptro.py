def encryption():
    print('encryption starting ...')
    msg = input('please enter the message that you want to encrypt : ')
    key = int(input('enterkey(1-94)'))
    etext = ''
    for i in range(len(msg)):
        t = (ord(msg[i])+key)
        if t > 126:
            t = t-127+32
        etext+=chr(t)
    print('your encryption message is : '+etext)

def decryption():
    print('decryption starting ...')
    msg = input('please enter the message that you want to decrypt : ')
    key = int(input('enterkey(1-94)'))
    etext = ''
    for i in range(len(msg)):
        t = (ord(msg[i])-key)
        if t < 32:
            t = t+127-32
        etext+=chr(t)
    print('your decryption message is : '+etext)    

def main():
    print('\nplease select a option :')
    choice = int(input('1.Encryption \n2.Decrption \n'))
    if choice == 1:
        encryption()
    elif choice == 2:
        decryption()
    else:
        print('get new brain and keyboard')   
main() 