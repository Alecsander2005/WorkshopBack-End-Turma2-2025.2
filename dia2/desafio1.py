import math 

def calcula_raiz_quadrada(num):
    return math.sqrt(num)


def main():
    valor = float(input("Digite um número: "))
    resultado = calcula_raiz_quadrada(valor)
    return f" o valor da raiz quadrada é: {resultado}"


print(main())
