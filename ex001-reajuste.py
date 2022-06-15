print("Reajuste salarial: ")
print("(1) = [2019: 3,43%]")
print("(2) = [2018: 2,07%]")
print("(3) = [2017: 6,58%]\n")
a = int(input("Escolha seu reajuste: "))
salario = float(input("Qual o seu sálario? "))
if (a == 1):
    reajuste = salario*0.0343 + salario
    print(reajuste)
elif (a == 2):
    reajuste = salario*0.0207 + salario
    print(reajuste)
elif (a == 3):
    reajuste = salario*0.0658 + salario
    print(reajuste)
else: 
    print("digite uma opção de reajuste válida!")
