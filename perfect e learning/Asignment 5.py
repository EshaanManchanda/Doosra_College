T= str(input())
# T="an apple a day keeps the doctor away"
T=sorted(list(T.lower()))
I=[]
for i in T:
    if i!=" ":
        I.append(i)
    k=sorted(list(set(I)))
    d={}
    print(k)
    for i in k:
        c=0
        for j in I:
            if i==j:
                c+=1
            d[i]=c
