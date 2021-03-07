def multipli (numero1,numero2):
    num1=int(numero1)
    num2=int(numero2)
    c=-1   #contador negativo
    d=1    #contador positivo
    f=num1
    if(c>num2):     #numero dois negativo
        while(c>num2):
            num1 = num1 +f
            c-=1
    else:               #numero dois positivo
        while(d!=num2):
            num1 = num1 +f
            d+=1
    if(f>0) and (num2>0):
        print(num1)
    elif(num2<0) or (num1<0):   #caso um deles for negativos
        print("-",num1)

multipli(5,3)
multipli(8,-7)