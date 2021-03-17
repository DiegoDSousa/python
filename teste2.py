def teste():
    #dic={}
    noa=[]
    telList = ['975318642', '234000111', '777888333', '911911911']
    nameList = ['Angelina', 'Brad', 'Claudia', 'Bruna']
    nome=input("Digite o nome: ")
    #for c in range (len(telList)):
        #dic[nameList[c]]=telList [c]
    for b in range(len(nome)):
        for h in range (len(nome)):
            for v in range(len(nameList)):
                if nameList[v] not in noa:
                #break
                    if nome[b] in nameList[v]:
                #print(dic[nameList[v]])
                        print("batata")
                        noa.append(nameList[v])
                #if nameList[v] in noa:
                    #break
    print(noa)
teste()