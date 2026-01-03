# Função para criptografar um texto usando XOR com uma chave numérica
# retornando o texto criptografado em bytes.
def cript_XOR(texto, chave):
    resultado = bytearray()
    for char in texto:
        # Pega o código ASCII do caractere e aplica o XOR com a chave.
        codigo_criptografado = ord(char) ^ chave
        resultado.append(codigo_criptografado)
    return bytes(resultado)


# Descriptografa um texto criptografado usando XOR.
# Como A ⊕ B ⊕ B = A, usar a mesma função recupera o original.
# Retorna o texto descriptografado.
def descript_XOR(texto_criptografado, chave):
    resultado = ""
    for byte in texto_criptografado:
        codigo_original = byte ^ chave
        resultado += chr(codigo_original)
    return resultado


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

    #Criptografar.
    texto_criptografado = cript_XOR(texto_original, chave_correta)
    print(f"\n2. CRIPTOGRAFADO (com chave {chave_correta}): ")
    print(f"Bytes: {list(texto_criptografado)}")
    print(f"Hexadecimal: {texto_para_hex(texto_criptografado)}")
    print(f"Tentativa de exibir como texto: {texto_criptografado}")

    # Descriptografar com chave correta.
    texto_recuperado = descript_XOR(texto_criptografado, chave_correta)
    print(f"\n3. DESCRIPTOGRAFADO COM CHAVE CORRETA ({chave_correta}): ", end="")
    print(f"{texto_recuperado}")
    print("✓    Sucesso! Texto original recuperado!")

    # Descriptografar com chave errada.
    texto_lixo = descript_XOR(texto_criptografado, chave_errada)
    print(f"\n4. DESCRIPTOGRAFADO COM CHAVE ERRADA ({chave_errada}): ", end="")
    print(f"{texto_lixo}")
    print(f"✗    Resultado inelegivel sem a chave correta!   ")

    # Demonstrando a propriedade A ⊕ B ⊕ B = A.
    print(f"\n5. DEMONSTRANDO A PROPRIEDADE A ⊕ B ⊕ B = A: ")
    exemplo = ord('H') # Equivalente ao primeiro caractere.
    print(f"Caractere original: 'H' = {exemplo}")
    print(f"'H' ⊕ {chave_correta} = {exemplo ^ chave_correta}")
    print(f"{exemplo ^ chave_correta} ⊕ {chave_correta} = {(exemplo ^ chave_correta) ^ chave_correta}")
    print(f"Resultado: {chr((exemplo ^ chave_correta) ^ chave_correta)}")


# Função principal.
def main():
    print("\n CIFRA XOR - MINI-PROJETO EDUCACIONAL\n")

    # Executa a demonstração básica
    demonstracao_basica()


if __name__ == "__main__":
    main()