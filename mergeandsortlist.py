L1=[1,5,7]
L2=[2,4,9]
L3=L1+L2
for i in range(len(L3)):
    for j in range(i+1,len(L3)):
        if L3[i]>L3[j]:
            L3[i],L3[j]=L3[j],L3[i]
print(L3)            
