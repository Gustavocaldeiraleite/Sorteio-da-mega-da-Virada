from random import choice

Number_all = []
number_sorteados = []
acertos = 0
aposta = []
cartela = " Sua cartela da MEGA DA VIRADA "
print(cartela.center(50, '-'))
print('\n', '=' * 45, '\n')
for c in range(1, 61):
    number = f'({c:02d}) ' if c < 10 or c % 10 != 0 else f'({c:02d})\n\n'
    print(number, end='')
print('=' * 45)
for i in range(1, 7):
    chute = int(input(f'Escolha um numero de 1 a 60 \n{i}/6 '))
    while chute in aposta or chute > 60:
        erro = 'Voce ja escolheu esse numero, tente outro' if chute in aposta else ('Numero invalido pois e maior que '
                                                                                    '60, tente outro')
        print(erro)
        chute = int(input(f'Escolha um numero de 1 a 60 \n{i}/6 '))
    aposta.append(chute)

for i in range(1, 61):
    Number_all.append(i)
for i in range(6):
    sorte = choice(Number_all)
    Number_all.remove(sorte)
    number_sorteados.append(sorte)

number_sorteados = sorted(number_sorteados)
aposta = sorted(aposta)

print('\n', '=' * 45, '\n')
for c in range(1, 61):
    if c in aposta:
        tabela = '(  ) ' if c < 10 or c % 10 != 0 else '(  )\n'
    else:
        tabela = f'({c:02d}) ' if c < 10 or c % 10 != 0 else f'({c:02d})\n\n'
    print(tabela, end='')
print('=' * 45)

for i in range(0, 6):
    if number_sorteados[i] in aposta:
        print(f'Voce acertou o numero: {number_sorteados[i]}')
        acertos += 1
if acertos == 6:
    print('Voce ganhou!!!!!!!')
else:
    print(f'Voce acertou: {acertos}')
if 5 == acertos == 4:
    print('Foi quase :( Tente na proxima')
print(number_sorteados)
print(aposta)
