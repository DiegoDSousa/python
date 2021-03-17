a=str(input("Digite: ")).lower()
b=str(input("Digite: ")).lower()
h=list(str())
f=""
for c in range (len(a)):
    s=0
    for d in range (len(b)):
        if (a[c] == b[d]):
            s+=1
    if s==0:
        h.append(a[c])
for c in range (len(b)):  #PARTBAIXO
    s=0
    for d in range (len(a)):
        if (b[c] == a[d]):
            s+=1
    if s==0:
        h.append(b[c])
f="".join(h)
print("A nova string é {0}".format(f))