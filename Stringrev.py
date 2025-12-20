n=input("enter a string")
# rev=n[1:4] #starts at 1 and ends at 4
# rev=n[2::] #default start 1 and default end is length of the string
# rev=n[::1] #default step is also 1
# rev=n[::-1] #for reverse step
# print(rev)

#without using slice
rev=""
for i in n:
    rev=i+rev
print(rev)    