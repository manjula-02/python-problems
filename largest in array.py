# arr=[5,8,4,13]
# print(max(arr)) #using built in max function 
# arr.sort() 
# print(arr[-1]) #that means first element in reverse
# largest=arr[0]
# for i in arr:
#     if i>largest:
#         largest=i

# print(largest)

#second largest

# arr.sort()
# print(arr[-2])

# arr.sort(reverse=True)
# print(arr[1])

#manual way
arr=[109,9,7,6,98,1]
largest=float('-inf')
second_largest=float('-inf')
for i in arr:
    if i>largest:
        largest=i
    elif i!=largest and i>second_largest:
        second_largest=i

print(second_largest)


