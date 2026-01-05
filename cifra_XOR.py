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


def modo_iterativo():
    print("\n" + "=" * 60)
    print("MODO INTERATIVO - EXPERIMENTE VOCÊ MESMO!")
    print("=" * 60)

    while True:
        print("""\nOpções:\n1 - Criptografar um texto\n2 - Descriptografar um texto\n3 - Sair""")
        opcao = input("\nEscolha uma opção: ").strip()

        match opcao:
            case '1':
                texto = input("\nDigite um texto para criptografar: ")
                try:
                    chave = int(input("Digite a chave (número inteiro 1-255): "))
                    if not 1 <= chave <= 255:
                        print("Chave deve estar entre 1 e 255!")
                        continue

                    criptografado = cript_XOR(texto, chave)
                    print(f"\n✓    Texto criptografado:")
                    print(f"Hexadecimal: {texto_para_hex(criptografado)}")
                    print(f"Bytes: {list(criptografado)}")
                    print(f"\nGuarde esta chave para descriptografar: {chave}")
                
                except ValueError:
                    print("Por favor digite um número válido!")
            
            case '2':
                try:
                    print("""\nDigite os bytes separados por espaço:\n(exemplo: 102 111 111)""")
                    bytes_input = input("Bytes: ").strip()
                    lista_bytes = [int(b) for b in bytes_input.split()]
                    texto_criptografado = bytes(lista_bytes)

                    chave = int(input("Digite a chave (número inteiro 1-255): "))
                    if not 1 <= chave <= 255:
                        print("Chave deve estar entre 1 e 255!")
                        continue

                    texto_recuperado = descript_XOR(texto_criptografado, chave)
                    print(f"\n✓    Texto descriptografado: '{texto_recuperado}'")
                
                except ValueError:
                    print("!!!    Formato inválido! Digite números separados por espaço.    !!!")
            
            case '3':
                print("\nAté logo!")
                return
            
            case _:
                print("!!!    Opção inválida!    !!!")


# Explica por que essa cifra não é segura.
def analise_seguranca():
    print("\n" + "=" * 60)
    print("POR QUE ESSA CIFRA NÃO É SEGURA?")
    print("=" * 60)
    print("""
1. CHAVE PEQUENA: Com apenas 255 valores possíveis (0-255),
um atacante pode testar todas as chaves rapidamente (força bruta).\n
2. CHAVE REUTILIZADA: A mesma chave é usada para cada caractere.
Isso cria padrões detectáveis.\n
3. ANÁLISE DE FREQUÊNCIA: Em textos longos, letras comuns (como 'e', 'a')
criam padrões que podem revelar a chave.\n
4. SEM AUTENTICAÇÃO: Não há forma de verificar se a mensagem
foi alterada durante a transmissão.\n
!!!    NUNCA USE ISSO EM PRODUÇÃO!    !!!\n
Para segurança real, use bibliotecas como:
- cryptography (Python)
- AES, RSA, etc.        
""")


# Função principal.
def main():
    print("\n CIFRA XOR - MINI-PROJETO EDUCACIONAL\n")

    # Executa a demonstração básica.
    demonstracao_basica()

    print("__" * 30)
    
    # Explica a segurança.
    analise_seguranca()

    print("__" * 30)

    # Pergunta se quer entrar no modo iterativo
    resposta = input("\nDeseja experimentar o modo iterativo? (s/n): ").strip().lower()
    if resposta == 's':
        modo_iterativo()
    else:
        print("\n Até logo!")


if __name__ == "__main__":
    main()