import random

print("Bem-vindo ao jogo de adivinhação!")

# Número secreto gerado aleatoriamente entre 1 e 10
numero_secreto = random.randint(1, 10)

# Jogador faz um palpite
palpite = int(input("Digite um número entre 1 e 10: "))

if palpite == numero_secreto:
    print("Parabéns! Você acertou o número secreto!")
elif abs(palpite - numero_secreto) == 1:
    print("Quase! Você errou por apenas 1.")
else:
    print(f"Você errou! O número secreto era {numero_secreto}.")
