#Questão 2 - Desafio Target.

#Declarando a função

def fibonacci(numero):
    
    x, y = 0, 1 # Atribuído duas variáveis com valores iniciais da sequencia de Fibonnaci
    while y < numero:   #Estrutura de repetição 
        x, y = y, x + y
    if y == numero:
        return True
    else:
        return False
    
# Programa principal

numero = int(input('Digite um número inteiro: '))

if fibonacci(numero):
    print(f"{numero} pertence à sequência de Fibonacci")
else:
    print(f"{numero} não pertence à sequência de Fibonacci")

