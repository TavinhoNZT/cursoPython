usuario = input('Nome de Usuario: ')
senha = input('Senha do Usuario: ')

usuario_bd = 'luiz'
senha_bd = '123456'

if usuario_bd == usuario and senha_bd == senha:
    print('Voce esta logado no sistema')
else:
    print('Usuario ou senha invalidos.')