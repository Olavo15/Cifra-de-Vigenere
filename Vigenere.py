def encrypt(text, key):
    cript = ""
    compri = len(key)
    for i in range(len(text)):
        Caract = text[i]
        if Caract.isalpha():
            key_char = key[i % compri]  # Corrigido o nome da variável
            mudanca = ord(key_char) - ord('A')
            if Caract.isupper():
                encrypted_char = chr(((ord(Caract) - ord('A') + mudanca) % 26) + ord('A'))
            else:
                encrypted_char = chr(((ord(Caract) - ord('a') + mudanca) % 26) + ord('a'))
        else:
            encrypted_char = Caract
        cript += encrypted_char
    return cript  

def decrypt(text, key):
    descri = ""
    compri = len(key)
    for i in range(len(text)):
        Caract = text[i]
        if Caract.isalpha():
            key_char = key[i % compri]  
            chave = ord(key_char) - ord('A')
            if Caract.isupper():
                decrypted_char = chr(((ord(Caract) - ord('A') - chave) % 26) + ord('A'))
            else:
                decrypted_char = chr(((ord(Caract) - ord('a') - chave) % 26) + ord('a'))
        else:
            decrypted_char = Caract
        descri += decrypted_char
    return descri 
