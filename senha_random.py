import string 
import random

continua = ''

while continua != 'N':
    
    tamanho_senha = int(input('\nQuantos caracteres terá a senha: '))

    senha_random = string.ascii_letters + string.digits #+ string.punctuation

    senha = ''
    
    for i in range(tamanho_senha):
        senha += random.choice(senha_random)
    
    print(f'\nSenha gerada:{senha}')
    
    continua = str(input('\nDeseja continuar? [S/N]: ')).strip().upper()

print(f'\nSenha escolhida: {senha}')