# Estágio Ribeirão Preto - 2024

Repositório de candidatura ao estágio.

A linguagem escolhida para desenvolver o questionário foi **Python**.

## Questão 1 [Código](https://github.com/andrebarceloschagas/estagio_riberao_2024/blob/main/questao_1.py)

Observe o trecho de código abaixo:

int INDICE = 13, SOMA = 0, K = 0;

enquanto K < INDICE faça
{
    K = K + 1;
    SOMA = SOMA + K;
}

imprimir(SOMA);

Ao final do processamento, qual será o valor da variável SOMA?

Resposta: **91**

    # Inicializa a variável INDICE com o valor 13
    indice = 13

    # Inicializa a variável SOMA com o valor 0
    soma = 0

    # Inicializa a variável K com o valor 0.
    k = 0

    # Entra em um loop enquanto o valor de K for menor que INDICE
    while k < indice:
        # Incrementa o valor de K em 1 a cada iteração
        k = k + 1
        # Adiciona o valor atual de K à variável SOMA
        soma = soma + k

    print(soma) # A saída será 91

## Questão 2 [Código](https://github.com/andrebarceloschagas/estagio_riberao_2024/blob/main/questao_2.py)

Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código.

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

## Questão 3 [Código](https://github.com/andrebarceloschagas/estagio_riberao_2024/blob/main/questao_3.py)

Descubra a lógica e complete o próximo elemento:  

a) 1, 3, 5, 7, **9** = A sequência é formada por números ímpares em ordem crescente.

    impar_crescente = []

    for i in range(1, 10):
        if i % 2 != 0:
            impar_crescente.append(i)

    print(impar_crescente)

b) 2, 4, 8, 16, 32, 64, **128** = A sequência é formada por números que são o dobro do número anterior.

    dobro_anterior = []

    for i in range(1, 8):
        dobro_anterior.append(2 ** i)

    print(dobro_anterior)

c) 0, 1, 4, 9, 16, 25, 36, **49** = A sequência é formada pelos quadrados dos números naturais em ordem crescente.

    quadrados_naturais = []

    for i in range(8):
        quadrados_naturais.append(i ** 2)

    print(quadrados_naturais)

d) 4, 16, 36, 64, **100** = A sequência é formada pelos quadrados dos números pares em ordem crescente.

    quadrados_pares = []

    for i in range(2, 11, 2):
        quadrados_pares.append(i ** 2)

    print(quadrados_pares)

e) 1, 1, 2, 3, 5, 8, **13** = A sequência é formada pelos números da sequência de Fibonacci.

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

f) 2, 10, 12, 16, 17, 18, 19, **200** = A sequência é formada por números que começam pela letra D.

    2 = Dois
    10 = Dez
    12 = Doze
    16 = Dezesseis
    17 = Dezessete
    18 = Dezoito
    19 = Dezenove
    **200 = Duzentos**

## Questão 4

Você está em uma sala com três interruptores, cada um conectado a uma lâmpada em uma sala diferente. Você não pode ver as lâmpadas da sala em que está, mas pode ligar e desligar os interruptores quantas vezes quiser. Seu objetivo é descobrir qual interruptor controla qual lâmpada.

Como você faria para descobrir, usando apenas duas idas até uma das salas das lâmpadas, qual interruptor controla cada lâmpada?

    Eu devo ligar o primeiro interruptor e esperar um pouco. Desligo o primeiro e ligo o segundo interruptor. Vou até a sala. Se a lâmpada estiver desligada e quente: corresponde ao primeiro interruptor. Se a lâmpada estiver acesa: corresponde segundo interrupitor. E se a lâmpada estiver apagada e fria: corresponde ao terceiro interrupitor.

## Questão 5 [Código](https://github.com/andrebarceloschagas/estagio_riberao_2024/blob/main/questao_5.py)

Escreva um programa que inverta os caracteres de um string.

IMPORTANTE:

a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;

b) Evite usar funções prontas, como, por exemplo, reverse;

    # Função que inverte os caracteres de uma string:

    def inverte_string(string):
        string_invertida = ""
        for i in range(len(string) - 1, -1, -1):
            string_invertida += string[i]
        return string_invertida

    string_informada = input("Informe uma string: ")

    print(f"A string invertida é: {inverte_string(string_informada)}")
