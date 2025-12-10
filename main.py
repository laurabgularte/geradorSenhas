import random
import string

def gerar_senha_forte(comprimento=12, usar_maiusculas=True, usar_numeros=True, usar_simbolos=True):
    """Gera uma senha forte e aleatória."""
    
    caracteres = string.ascii_lowercase 
    
    if usar_maiusculas:
        caracteres += string.ascii_uppercase
    if usar_numeros:
        caracteres += string.digits
    if usar_simbolos:
     
        caracteres += '!@#$%^&*()_+-=[]{}|;:,.<>?' 
 
    if not caracteres:
        raise ValueError("Nenhum conjunto de caracteres selecionado para gerar a senha.")

    senha = []
    
    if usar_maiusculas:
        senha.append(random.choice(string.ascii_uppercase))
    if usar_numeros:
        senha.append(random.choice(string.digits))
    if usar_simbolos:
        senha.append(random.choice('!@#$%^&*()_+-=[]{}|;:,.<>?'))
    

    caracteres_restantes = comprimento - len(senha)
    senha.extend(random.choices(caracteres, k=caracteres_restantes))
    
    
    random.shuffle(senha)
    
    
    return "".join(senha)


senha1 = gerar_senha_forte(comprimento=16, usar_simbolos=True)
print(f"Senha Forte (16 caracteres): {senha1}")

senha2 = gerar_senha_forte(comprimento=10, usar_simbolos=False)
print(f"Senha Média (10 caracteres): {senha2}")