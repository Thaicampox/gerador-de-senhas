import random
import string

def gerar_senha(tamanho=12):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

if __name__ == "__main__":
    try:
        tamanho = int(input("Digite o tamanho da senha desejada: "))
        senha_gerada = gerar_senha(tamanho)
        print(f"Sua senha gerada: {senha_gerada}")
    except ValueError:
        print("Erro: Digite um número válido para o tamanho da senha.")
