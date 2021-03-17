#Diego sousa
f=open("words.txt","r")
dic={}
a=f.read()
b=a.split()
for c in range (len(b)):
    if b[c] in b:
        nr=b.count(b[c])#numero repeticoes
        dic[b[c]]=nr
chaves=list(dic.keys())
valores=list(dic.values())
for v in range(len(chaves)):
    print("{}:{:2}".format(chaves[v],valores[v]))