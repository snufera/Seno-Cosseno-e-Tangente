print("\nSeja muito bem vindo!\nEsse programa calcula o Seno, Cosseno e Tangente do ângulo informado!\n")
print("ATENÇÃO!!! UTILIZE APENAS NÚMEROS!!!\n")

from math import sin, cos, tan, radians

x = float(input("Informe o ângulo que irá ser calculado: "))
print("\n1 = Seno | 2 = Cosseno | 3 = Tangente | 4 = Todos")
option = input("O que você quer calcular? (1) (2) (3) (4) : ")

seno = sin(radians(x))
cosseno = cos(radians(x))
tangente = tan(radians(x))

if option == "1":
    print(f"\nSeno: {seno:.2f}.\n")

elif option == "2":
    print(f"\nCosseno: {cosseno:.2f}.\n")

elif option == "3":
    print(f"\nTangente: {tangente:.2f}.\n")

elif option == "4":
    print(f"\nSeno: {seno:.2f}.\nCosseno: {cosseno:.2f}.\nTangente: {tangente:.2f}.\n")

else:
    print("\nTecla inválida!\n")
