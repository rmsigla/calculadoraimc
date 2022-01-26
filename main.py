### Calculo de IMC Romulo Amorim ###

### Variaveis de Classificação ###
# Magreza = Menor que 18.5
# Normal = Entre 18.5 e 24.9
# Sobrepeso I = Entre 25.0 e 29.9
# Obesidade II = Entre 30.0 e 39.9
# Obesidade Grave III = Maior que 40.0

print("Olá!")
print("Bem vindo a Calculadora de Índice de Massa Corporal - IMC\n")

nome = (input("Qual seu nome? "))
altura = float(input("Digite sua Altura em cm: "))
peso = float(input("Digite seu Peso em kg: "))

imc = peso / (altura / 100)**2

print("\n")

print(nome, " seu índice de Massa Corporal é: %.4f" % imc)

if imc < 18.5:
    print("Sua classificação é de Magreza")

elif imc >= 18.5 and imc < 24.9:
    print("Sua classificação é Normal")

elif imc >= 25.0 and imc < 29.9:
    print("Sua classificação é de Sobrepeso I")

elif imc >= 29.9 and imc < 30.0:
    print("Sua classificação é de Sobrepeso II")

else:
    print("Sua classificação é de Sobrepeso Grave III")

print("\n")

print("Obrigado por utilizar nosso aplicativo. Volte sempre!")
