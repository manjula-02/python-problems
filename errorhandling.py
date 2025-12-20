try:
    f=open("demo.txt","r")
    f.read()
    f.close()
except FileNotFoundError:
    print("error:file doesn't exist")
except PermissionError:
    print("error:you do not have access")
except Exception as e:
    print("unexpected error",e) 
    # print(e)     #prints the exception error
