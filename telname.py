def teste():
    dic={}#dicionario
    telList = ['975318642', '234000111', '777888333', '911911911']
    nameList = ['Angelina', 'Brad', 'Claudia', 'Bruna']
    for c in range (len(telList)):
        dic[telList[c]]=nameList[c]
    #print(dic)
    tel=(input("Digite: "))
    if tel in telList:
        #print(numero,"->",dic[numero])
        return dic[tel]
    else:
       # print("O numero {} nao se encontra na lista".format(numero))
        return tel
print(teste())