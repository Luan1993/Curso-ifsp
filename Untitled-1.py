'''nome = "Carlos"
idade = 30
saldo_conta = 1250.75

#jeito antigo
print("o usuario",nome, "tem", idade, "anos e saldo de", saldo_conta)

#com f-string (muito  melhor!)
print(f"O usuario{nome} tem {idade} anos e saldo de {saldo_conta}")

'''
frase = " bem-vindo ao curso de Python! "
print(f"Original: '{frase}'")
print(f"Maiúsculas: '{frase.upper()}'")
print(f"Minúsculas: '{frase.lower()}'")
print(f"Capitalizada: '{frase.strip().capitalize()}'")
print(f"Troca: '{frase.replace('Python','Django')}'")
print(f"Começa com 'bem'? {frase.strip().startswith('bem')}")