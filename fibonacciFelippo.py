
print("-~"*25)
n = int(input('Termo que deseja encontrar: ')) #Ausencia da declaração do tipo da variavel.
ultimo = 1 #o primeiro termo da sequencia não é 1, e sim 0.
penultimo = 1
if n == 1: #condicional que printa apenas o 1ºtermo.
    termo = ultimo
    print(ultimo)
elif n == 2 or n == 3: #condicional que printa apenas o 2ºtermo.
    termo = penultimo
    print(penultimo)
else:
    count = 4
    while count <= n:
        termo = (ultimo) + (penultimo)
        penultimo = ultimo
        ultimo = termo
        count+= 1
print("Seu termo número {} é ({}) \n".format(n, termo)) 

# A função 'print' estava dentro do while gerando uma sequência de valores, a qual não era o objetivo inicial
#do código. O comando do código é para encontrar apenas um único e especÍfico termo da sequência de Fibonacci.

# E como um erro geral, as linhas de códigos estavam terminadas em ';'. Um erro, visto que em Python não   
#há a necessidade. 

print("-~"*25)
print("linhas extra de código\n")
print("[1]: sequencia de Fibonacci\n", "[2]: Termo especifico de Fibonacci")
extra = int(input('escolha sua opção: '))
print('-~'*25)
if extra == 1:
    sequencia = int(input("Quantos termos da sequência de Fibonacci deseja mostrar? "))
    print('-'*50)
    termo1 = 0
    termo2 = 1
    count = 3
    print("{} -> {} -> ".format(termo1, termo2), end='')
    while count <= sequencia:
        termo3 = termo1 + termo2
        print('{} -> '.format(termo3), end='') 
        termo1 = termo2
        termo2 = termo3
        count += 1
    print("Fim da sequência")
    print('-'*50)
