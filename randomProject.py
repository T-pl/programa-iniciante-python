#Primeiro Projeto
import random 

print("Bem-vindo ao jogo 'Adivinhe o Número!' \n")

print("Um sistema automático irá gerar um número aleatório de 0 a 100.\n")

print("Você tem 10 chances de acertar qual número foi gerado. Vamos começar.\n")

n = int(random.randint(0, 100)) #Número gerado pela função random

tentativas = 0

while tentativas <= 10:
    p = int(input("Adivinhe qual número foi gerado: \n")) #Tentativa do usuário
     
    if p < n:
     print('Está frio. Tente Outra vez.')
     tentativas = tentativas + 1
    elif p > n:
     print('Está Quente. Tente Outra vez.')
     tentativas = tentativas + 1
    elif p == n:
     print("Você acertou. Parabéns! O número é {} e acertou com {} tentativas.".format(p,tentativas))
     break
else:
    print("Acabaram suas chances. Recomece o jogo.")

         
    
      


        







