
    #diego Sousa
# Convert a telephone number into corresponding name, if on list.
# (If not on list, just return the number itself.)
def telToName(tel, telList, nameList):
    try:
        pos = telList.index(tel)
        name = nameList[pos]
    except ValueError:
        name = tel
    return name
# Return list of telephone numbers corresponding to names containingpartName.
def nameToTels(partName, telList, nameList):
    noa=[]
    #telList = ['975318642', '234000111', '777888333', '911911911']
    #nameList = ['Angelina', 'Brad', 'Claudia', 'Bruna']
    #nome=input("Digite o nome: ")
    #for c in range (len(telList)):
        #dic[nameList[c]]=telList [c]
    for b in range(len(name)):
        for h in range (len(name)):
            for v in range(len(nameList)):
                if nameList[v] not in noa:
                #break
                    if name[b] in nameList[v]:
                #print(dic[nameList[v]])
                        noa.append(nameList[v])
                #if nameList[v] in noa:
                    #break
    return noa
# Lists of telephone numbers and names
telList = ['975318642', '234000111', '777888333', '911911911']
nameList = ['Angelina', 'Brad', 'Claudia', 'Bruna']
# Test telToName:
#tel = input("Tel number? ")
#print( telToName(tel, telList, nameList) )
#print( telToName('234000111', telList, nameList) == "Brad" )
#print( telToName('222333444', telList, nameList) == "222333444" )
# Test nameToTels:
name = input("Name? ")
print( nameToTels(name, telList, nameList) )
print( nameToTels('Clau', telList, nameList) == ['777888333'] )
print( nameToTels('Br', telList, nameList) == ['234000111','911911911'] )