numero_inteiro = input('Digite um numero inteiro: ')

if not numero_inteiro.isdigit():
    print('Isso nao e um numero inteiro.')
else:
    numero_inteiro = int(numero_inteiro)
    
    if not numero_inteiro % 2 == 0:
        print(f'{numero_inteiro} e impar')
    else:
        print(f'{numero_inteiro} e par.')

horario = input('Digite um horario (0-23): ')

if horario.isdigit():
    horario = int(horario)
    
    if horario < 0 or horario > 23:
        print("Horario deve estar entre 0 e 23")
    else:
        if horario <= 11:
            print('Bom Dia.')
        elif horario <= 17:
            print('Boa Tarde.')
        else:
            print('Boa Noite.')
    
else:
    print("Por favor, digite um horario entre 0  e 23.")

nome = input('Digite seu nome: ')
tamanho = len(nome)

if tamanho <= 4:
    print('Seu nome e curto')
elif tamanho <= 6:
    print('Seu nome e normal')
else:
    print('Seu nome e muito grande')