""" 
2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores
(exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número,
ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.   

IMPORTANTE:  

Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;
"""

# Código:

# Função que verifica se um número pertence à sequência de Fibonacci:
def fibonacci(numero):
    a, b = 0, 1
    while b < numero:
        a, b = b, a + b
    return b == numero

# Informe o número para receber a entrada do usuário
numero_informado = int(input("Informe um número: "))

# Bloco condicional para verificar se pertence ou não a sequência Fibonacci 
if fibonacci(numero_informado):
    print(f"O número {numero_informado} PERTENCE à sequência de Fibonacci.")
else:
    print(f"O número {numero_informado} NÃO PERTENCE à sequência de Fibonacci.")
