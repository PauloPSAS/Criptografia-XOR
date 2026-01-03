# Função para criptografar um texto usando XOR com uma chave numérica
# retornando o texto criptografado em bytes.
def cript_XOR(texto, chave):
    resultado = bytearray()
    for char in texto:
        # Pega o código ASCII do caractere e aplica o XOR com a chave.
        codigo_criptografado = ord(char) ^ chave
        resultado.append(codigo_criptografado)
    return bytes(resultado)


# Converte bytes para representação hexadecimal legível.
def texto_para_hex(texto_bytes):
    return ' '.join(f'{b:02x}' for b in texto_bytes)



# Função para fazer a demonstração básica da cifra de XOR.
def demonstracao_basica():
    print("=" * 60)
    print("DEMONSTRAÇÃO BÁSICA - CIFRA XOR")
    print("=" * 60)

    texto_original = "Hello World!"
    chave_correta = 42
    chave_errada = 99

    print(f"\n1. TEXTO ORIGINAL: ", end="")
    print(f"'{texto_original}'")
    print(f"Códigos ASCII: {[ord(c) for c in texto_original]}")

    #Criptografar
    texto_criptografado = cript_XOR(texto_original, chave_correta)
    print(f"\n2. CRIPTOGRAFADO (com chave {chave_correta}): ")
    print(f"Bytes: {list(texto_criptografado)}")
    print(f"Hexadecimal: {texto_para_hex(texto_criptografado)}")
    print(f"Tentativa de exibir como texto: {texto_criptografado}")


# Função principal.
def main():
    print("\n CIFRA XOR - MINI-PROJETO EDUCACIONAL\n")

    # Executa a demonstração básica
    demonstracao_basica()


if __name__ == "__main__":
    main()