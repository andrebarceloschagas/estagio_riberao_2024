"""
5) Escreva um programa que inverta os caracteres de um string. 


IMPORTANTE: 

a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código; 

b) Evite usar funções prontas, como, por exemplo, reverse;
"""

# Código:

# Função que inverte os caracteres de uma string:

def inverte_string(string):
    string_invertida = ""
    for i in range(len(string) - 1, -1, -1):
        string_invertida += string[i]
    return string_invertida

string_informada = input("Informe uma string: ")

print(f"A string invertida é: {inverte_string(string_informada)}")
