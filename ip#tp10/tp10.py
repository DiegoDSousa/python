def displayinventory(inventario):
    chaves=list(inventario.keys())
    valor=list(inventario.values())
    print("Inventario")
    for c in range (len(chaves)):
        print(valor[c],chaves[c])
inventario={}
while True:
    item=str(input("Digite o item: "))
    quan=int(input("Qual a quantidade: "))
    con=str(input("Continuar: [s/n]"))
    inventario[item]=quan
    if con=="n":
        break
displayinventory(inventario)