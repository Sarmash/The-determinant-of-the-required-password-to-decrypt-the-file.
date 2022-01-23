from simplecrypt import encrypt, decrypt, DecryptionException

with open('encrypted.bin', 'rb') as inp, open('passwords.txt', 'r') as inp1:
    encrypted = inp.read()
    decrypted = [line.rstrip() for line in inp1.readlines()]
    for i in decrypted:
        try:
            print()
            print(decrypt(i, encrypted))
            print(i, 'correct password')
            print()
        except DecryptionException:
            print(i, 'invalid password')