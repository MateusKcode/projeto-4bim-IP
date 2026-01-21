import string
import random

def gerador_senhas(comprimento):
    chars = string.ascii_letters + string.digits + string.punctuation
    senha = []
    for i in range(comprimento):
        pool = random.choice(chars)
        senha.append(pool)
    
    return ''.join(senha)

senha = gerador_senhas(8)