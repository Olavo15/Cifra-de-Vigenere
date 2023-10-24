from Vigenere import encrypt, decrypt

def main():
    palavra = input("Escolha 'E' para cifrar ou 'D' para decifrar: ")
    if palavra.upper() == 'E':
        texto1 = input("Digite o texto a ser cifrado: ")
        chave = input("Digite a chave de cifra: ")
        cript = encrypt(texto1, chave)
        print(f"Texto cifrado: {cript}")
    elif palavra.upper() == 'D':
        texto2 = input("Digite o texto cifrado: ")
        chave = input("Digite a chave de cifra: ")
        descri = decrypt(texto2, chave)
        print(f"Texto decifrado: {descri}")
    else:
        print("Escolha inválida.")

if __name__ == "__main__":
    main()
    
   # Alysson, Aristoteles, Pierre, Guilherme e Olavo
