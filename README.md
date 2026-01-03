# Cifra XOR

Este projeto é um mini laboratório educacional para explorar o operador lógico XOR
(eXclusive OR) e sua aplicação em criptografia simétrica básica.

## Sobre XOR?

O operador XOR retorna verdadeiro quando exatamente uma das entradas é verdadeira.

Tabela verdade:

A | B | A ⊕ B
--|---|------
0 | 0 | 0
0 | 1 | 1
1 | 0 | 1
1 | 1 | 0

Propriedades importantes:

- A ⊕ A = 0
- A ⊕ 0 = A
- A ⊕ B ⊕ B = A

## A cifra XOR

A cifra XOR funciona aplicando o operador XOR byte a byte:

C = P ⊕ K  
P = C ⊕ K  

Ou seja, cifrar e decifrar é a mesma operação.