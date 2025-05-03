import math
import random


def gerar_placa():
    """
    Gera uma placa de carro no formato ABC123.
    """
    letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    # Gera as letras
    parte1 = "".join(random.choices(letras, k=3))
    
    # Gera os números
    numero1 = random.randint(0, 9)
    numero2 = random.randint(0, 9)
    numero3 = random.randint(0, 9)

    # Monta a placa   
    placa = f"{parte1}{numero1}{numero2}{numero3}"
    
    return placa


base = set() # evitar duplicadas
# 26 letras
# 10 números
# 26^3 * 10^2 = 1757600
# 1757600 placas possíveis

limite = 100
while True:
    # Gera uma placa
    placa = gerar_placa()
    
    # Exibe a placa
    print(placa)
    # no usar != para comparar string con listas
    # sino in para comparar string con listas 
    if placa not in base:
        base.add(placa)
    else:
        print("Placa já existe")
        break

