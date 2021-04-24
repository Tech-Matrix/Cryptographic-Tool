def egcd(a, b):
    x, y, u, v = 0, 1, 1, 0
    while a != 0:
        q, r = b // a, b % a
        m, n = x - u * q, y - v * q
        b, a, x, y, u, v = a, r, u, v, m, n
    gcd = b
    return gcd, x, y


def modinv(a, m):
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        return None
    else:
        return x % m


def affine_encrypt(text):
    key = [17, 20]
    result= ''.join([chr(((key[0] * (ord(t) - ord('A')) + key[1]) % 26) + ord('A')) for t in text.upper().replace(' ', '')])

    return 'Encrypted Text: '+result


def affine_decrypt(text):
    key = [17, 20]
    result= ''.join([chr(((modinv(key[0], 26) * (ord(c) - ord('A') - key[1])) % 26) + ord('A')) for c in text])
    return 'Decrypted text: '+result

text = input('Enter the text: ')
affine_encrypted_text = affine_encrypt(text)
print(affine_encrypted_text)
text = input('Enter the cipher: ')
affine_decrypted_text=affine_decrypt(text)
print(affine_decrypted_text)
