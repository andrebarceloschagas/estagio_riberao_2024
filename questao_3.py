
# 3) Descubra a lógica e complete o próximo elemento:  

# Código:

# a) 1, 3, 5, 7, 9 = A sequência é formada por números ímpares em ordem crescente.

impar_crescente = []

for i in range(1, 10):
    if i % 2 != 0:
        impar_crescente.append(i)

print(impar_crescente)

# b) 2, 4, 8, 16, 32, 64, 128 = A sequência é formada por números que são o dobro do número anterior.

dobro_anterior = []

for i in range(1, 8):
    dobro_anterior.append(2 ** i)

print(dobro_anterior)

# c) 0, 1, 4, 9, 16, 25, 36, 49 = A sequência é formada pelos quadrados dos números naturais em ordem crescente.

quadrados_naturais = []

for i in range(8):
    quadrados_naturais.append(i ** 2)

print(quadrados_naturais)

# d) 4, 16, 36, 64, 100 = A sequência é formada pelos quadrados dos números pares em ordem crescente.

quadrados_pares = []

for i in range(2, 11, 2):
    quadrados_pares.append(i ** 2)

print(quadrados_pares)

# e) 1, 1, 2, 3, 5, 8, 13 = A sequência é formada pelos números da sequência de Fibonacci.

def fibonacci(numero):
    a, b = 0, 1
    while b < numero:
        a, b = b, a + b
    return b == numero

fibonacci_sequence = []

for i in range(1, 14):
    if fibonacci(i):
        fibonacci_sequence.append(i)

print(fibonacci_sequence)

# f) 2, 10, 12, 16, 17, 18, 19, 200 = A sequência é formada por números que começam pela letra D.

# A sequência é formada por números que começam pela letra D.
# 2 = Dois
# 10 = Dez
# 12 = Doze
# 16 = Dezesseis
# 17 = Dezessete
# 18 = Dezoito
# 19 = Dezenove
# 200 = Duzentos
