KPI = 1000

nome = input("Escreva o seu nome: ")

if nome.isdigit():
    print("Nome errado!")
    exit()
elif len(nome) == 0:
    print("Você não digitou nada!")
    exit()
elif nome.isspace():
    print("Está com espaço vazio!")
    exit()

try:
    salario = float(input("Digite o valor do seu salario: "))
    bonus = float(input("Digite o valor do bonus recebido: "))
    bonus_final = KPI + salario * bonus
    print(f"O usuario {nome} possui o bonus de {bonus_final}")

except ValueError as e:
    print(e)
    
