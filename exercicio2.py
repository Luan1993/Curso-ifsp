usuario = input('Insira o usuario')
senha = input("insira a senha")

if usuario == 'admin' and senha == "12345":
    print('Login bem-sucedido')

elif usuario != 'admin':
    print("usuario invalido")

elif senha != "12345":
    print("senha incorreta")


    