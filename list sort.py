li=[9,6,3,4,546]
for i in range(len(li)):
    for j in range(i+1,len(li)): #for comparing with remaining
        if li[i]>li[j]:
            # li[i],li[j]=li[j],li[i] #swapping item if it is larger
            temp=li[i]    #with using temporary variable
            li[i]=li[j]
            li[j]=temp
                   
print(li)            