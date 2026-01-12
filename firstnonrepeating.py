
def firstnonrepeating(s):
   for i in range(len(s)):
     if s.count(s[i])==1:
           return i 
s=input("enter string :")
print(firstnonrepeating(s))
