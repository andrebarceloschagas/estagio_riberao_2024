"""
1) Observe o trecho de código abaixo: 

 	int INDICE = 13, SOMA = 0, K = 0; 

 	enquanto K < INDICE faça 

	{ 

		K = K + 1; 

		SOMA = SOMA + K; 

	} 

 	imprimir(SOMA); 

Ao final do processamento, qual será o valor da variável SOMA? 
"""

# Código: 

# Inicializa a variável INDICE com o valor 13
indice = 13

# Inicializa a variável SOMA com o valor 0. Esta variável será usada para acumular a soma
soma = 0

# Inicializa a variável K com o valor 0. Esta variável será usada como contador
k = 0

# Entra em um loop enquanto o valor de K for menor que INDICE
while k < indice:
    # Incrementa o valor de K em 1 a cada iteração
    k = k + 1

    # Adiciona o valor atual de K à variável SOMA
    soma = soma + k

# Imprime o valor final da variável SOMA
print(soma) # A saída será 91
