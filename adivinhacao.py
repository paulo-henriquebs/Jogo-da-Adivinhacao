import random

print("---------------------------------  ")
print("VOCÊ ESTÁ NO JOGO DA ADIVINHAÇÃO!")
print("---------------------------------  \n")

print(" | QUAL O SEU NÍVEL DE ADIVINHAÇÃO? | ")
dificuldade = input("Iniciante, Amador ou Profisssional? ")

tentativas_maximas = 5
if dificuldade == "Profissional":
  tentativas_maximas == 3
elif dificuldade == "Amador":
  tentativas_maximas == 5
elif dificuldade == "Iniciante":
  tentativas_maximas = 7
else:
  print (" --> NÍVEL DE DIFICULDADE NÃO DEFINIDA, A DIFICULDADE FOI AJUSTADA AUTOMATICAMENTE PARA O NÍVEL AMADOR.")


#Vamos ter uma randomização do número, para isso, importamos a biblioteca "random" que gera um número aleatório. Chamamos a biblioteca com o random. e em seguida o tipo de número que queremos, nesse caso o "randInt" por ser um número inteiro. Dentro dos parênteses colocamos um valor mínimo e um valor máximo possível. 

numero_secreto = random.randint(1,100)
tentativas = 1

#As estruturas de repetição servem para estipular um número de tentativas, então basicamente o que esse while diz: "enquanto o número de tentativas for menor ou igual a 3."

while tentativas <= tentativas_maximas:
  print("\n --> ⚠️ ATENÇÃO! VOCÊ ESTÁ NA TENTATIVA", tentativas, "de", tentativas_maximas, ":")
  numero_usuario = int(input("\n --> CHUTE O NÚMERO SECRETO: "))

  if numero_secreto == numero_usuario:
    print("--> RESPOSTA CORRETA! VOCÊ ACERTOU O NÚMERO SECRETO!! ✅")
    break
  elif numero_secreto > numero_usuario:
    print(" --> O NÚMERO SECRETO É MAIOR DO QUE O QUE VOCÊ DIGITOU! ➕")
  else:
    print(" --> O NÚMERO SECRETO É MENOR DO QUE O QUE VOCÊ DIGITOU! ➖")

  tentativas += 1

#fora da estrutura de repetição, utilizamos estruturas condicionais para mostrar ao usuário uma mensagem caso ele exceda o número de tentativas.
if tentativas > tentativas_maximas:
  print("\n\n --> O JOGO ACABOU, VOCÊ PERDEU. O NÚMERO SECRETO ERA", numero_secreto)
