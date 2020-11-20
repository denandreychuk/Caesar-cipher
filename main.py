def encrypt(text, k):
    result = ""

    for i in range(len(text)):
        char = text[i]

        if char.isupper():
            result += chr((ord(char) + k - 65) % 26 + 65)
        else:
            result += chr((ord(char) + k - 97) % 26 + 97)

    return result

def decrypt(text, k):
    result = ""

    for i in range(len(text)):
        char = text[i]

        if char.isupper():
            result += chr((ord(char) - k - 65) % 26 + 65)
        else:
            result += chr((ord(char) - k - 97) % 26 + 97)

    return result

def analyse(ciphertext):
    uniqChars = "".join(set(ciphertext))

    freq = dict()
    for l in uniqChars:
        freq[l] = ciphertext.count(l) / float(len(ciphertext))

    freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    
    print("Breaking...")
    for char in freq:
        print(f"freq {char[1]}, char {char[0]}")
        if char[0].isupper():
            key = ord(char[0]) - 65 - 4
            result = decrypt(ciphertext, key)
            print(f'Decrypted text: {result}')
        else:
            key = ord(char[0]) - 97 - 4
            result = decrypt(ciphertext, key)
            print(f'Decrypted text: {result}')

if __name__ == '__main__':
    encrypted = encrypt('heelo', 12)
    print(f'Encrypted text: {encrypted}')

    decrypted = decrypt(encrypted, 12)
    print(f'Decrypted text: {decrypted}')

    analyse(encrypted)

