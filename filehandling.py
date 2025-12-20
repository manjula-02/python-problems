f=open("demo.text","r")
# content=f.read()

# content=f.readlines() #in list format

# content=f.readline()  #first line of content


# for line in f:
#     print(line,end="") #to print each line

content=f.readlines()
print(content[2])  #for a specific line fisrt we convert it to list using readlines

f.close()