# using with statement 

with open("data.txt","r")as file:
    content = file.read()
    print(content)

    #Create New File
    file = open("newfile.txt","x")
    file.close()

   