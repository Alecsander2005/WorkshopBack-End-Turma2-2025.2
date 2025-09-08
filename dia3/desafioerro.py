"""
1)

print("Olá, mundo!" 

não está fechando o parêntese corretamente

2) print(nome)

não está definido

3) def somar(a, b):
    return a + b

resultado = somar(10, "5")
print(resultado)

4) numeros = [10, 20, 30]
indice = int(input("Digite um índice para acessar a lista: ")) 

print(numeros[indice])

5) def dividir(a, b):
    return a / b

num1 = input("Digite o primeiro número: ")
num2 = input("Digite o segundo número: ")

resultado = dividir(int(num1), int(num2))
print(f"Resultado: {resultado}")

6) dados = {
    "nome": "Isaac ",
    "idade": 25,
    "cidade": "São Paulo"
}

chave = input("Digite a chave que deseja acessar: ")

print(f"O valor da chave '{chave}' é: {dados[chave]}")

7) def validar_idade(idade)
    if idade < 0 or idade > 120:
        raise ValueError("A idade deve estar entre 0 e 120 anos!")  # Erro personalizado
    return f"Idade válida: {idade}"

idade = int(input("Digite sua idade: "))
print(validar_idade(idade))
"""
nome = input("Digite seu nome: ")

print(nome)

try:
    def somar(a, b):
        return a + b
    
    resultado = somar(10, "5")

    print(resultado)
except TypeError:
    print("Erro: Não é possível somar um número com uma string.")

try:
    numeros = [10, 20, 30]
    indice = int(input("Digite um índice para acessar a lista: ")) 

    print(numeros[indice])

except IndexError:
    print("Erro: Índice fora da lista.")

try:
    def dividir(a, b):
        return a / b

    num1 = input("Digite o primeiro número: ")
    num2 = input("Digite o segundo número: ")

    resultado = dividir(int(num1), int(num2))
    print(f"Resultado: {resultado}")

except ZeroDivisionError:
    print("Erro: Divisão por zero não é permitida.")
except ValueError:
    print("Erro: Entrada inválida. Por favor, digite números válidos.")

# com dados.get
dados = {
    "nome": "Isaac ",
    "idade": 25,
    "cidade": "São Paulo"
}

chave = input("Digite a chave que deseja acessar: ")

valor = dados.get(chave, "Chave não encontrada no dicionário.")
print(f"O valor da chave '{chave}' é: {valor}")

# com try e except
try:
    dados = {
        "nome": "Isaac ",
        "idade": 25,
        "cidade": "São Paulo"
}

    chave = input("Digite a chave que deseja acessar: ")

    print(f"O valor da chave '{chave}' é: {dados[chave]}")
except KeyError:
    print("Erro: Chave não encontrada no dicionário.")

def validar_idade(idade):
    while True:
        try:
            idade = int(input("Idade inválida. Digite uma idade entre 0 e 120 anos: "))
            if 0 <= idade <= 120:
                break
        except ValueError:
            print("Erro: Por favor, digite um número válido.")
    return f"Idade válida: {idade}"

idade = int(input("Digite sua idade: "))
print(validar_idade(idade))