"""
DESAFIO PYTHON: Verificador de Números Primos

Objetivo: Criar uma função que verifique se um número é primo.

Um número primo é aquele que só é divisível por 1 e por ele mesmo.

Exemplos:
- 2, 3, 5, 7, 11 são primos
- 4, 6, 8, 9, 10 não são primos
"""

# ============= DESAFIO =============
# Escreva uma função chamada 'eh_primo' que:
# 1. Recebe um número inteiro como parâmetro
# 2. Retorna True se o número é primo
# 3. Retorna False se o número não é primo

def eh_primo(numero):
    """
    Verifique se um número é primo.
    
    Args:
        numero (int): O número a ser verificado
    
    Returns:
        bool: True se é primo, False caso contrário
    """
    # TODO: Implemente a solução aqui
    pass


# ============= TESTES =============
# Descomente os testes abaixo para verificar sua solução:

if __name__ == "__main__":
    # Testes
    print("Testando a função eh_primo():")
    print(f"eh_primo(2) = {eh_primo(2)}")      # Esperado: True
    print(f"eh_primo(3) = {eh_primo(3)}")      # Esperado: True
    print(f"eh_primo(4) = {eh_primo(4)}")      # Esperado: False
    print(f"eh_primo(5) = {eh_primo(5)}")      # Esperado: True
    print(f"eh_primo(10) = {eh_primo(10)}")    # Esperado: False
    print(f"eh_primo(17) = {eh_primo(17)}")    # Esperado: True
    print(f"eh_primo(1) = {eh_primo(1)}")      # Esperado: False


# ============= DICA =============
# Se precisar de ajuda, aqui está um passo a passo:
# 1. Números menores que 2 não são primos
# 2. O número 2 é primo
# 3. Para outros números, verifique se há algum divisor entre 2 e a raiz quadrada do número
# 4. Se não houver divisor, é primo!

"""
SOLUÇÃO (não olhe antes de tentar!):

def eh_primo(numero):
    if numero < 2:
        return False
    
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    
    return True
"""
