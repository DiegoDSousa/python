import os
def maior(valores):
    maior= max(valores)
    print("O maior valor digitado foi {0}!".format(maior))

def menor(valores):
    menor=min(valores)
    print("O menor valor digitado foi {0}!".format(menor))

c=0
valores=[]
while(c!="n"):
    n=int(input("Digite um numero: "))
    while(n<2):
        n=int(input("Digite um valor maior ou igual a dois:"))
    valores.append(n)
    c=str(input("Continuar? [s/n] "))
    if(c=="n"):
        break
    os.system('cls' if os.name == 'nt' else'clear')

os.system('cls' if os.name == 'nt' else'clear')
print(valores)
maior(valores)
menor(valores)