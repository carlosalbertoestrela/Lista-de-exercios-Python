"""
 12) Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10.
 O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:
    Tabuada de 5:
    5 X 1 = 5
    5 X 2 = 10
    ...
    5 X 10 = 50
"""
num = int(input('Digite um número para ver sua tabuada: '))
print(f'{f"Tabuada de {num}!":^30}\n{"-="*15}')
for n in range(1, 11):
    print(f"{f'{n:3} x {num:3} = {num * n:4}':^30}")
print('-='*15)
