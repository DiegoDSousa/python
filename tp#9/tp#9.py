def cumsum():
    numeros=[]
    lf=[]
    while True:
        num=int(input("Digite um valor:"))
        numeros.append(num)
        lf.append(sum(numeros))
        con=str(input("Continuar: [s/n]"))
        if( con=='n'):
            break
    print(lf)
cumsum()
