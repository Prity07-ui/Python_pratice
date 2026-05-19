#Append File

file = open("data.txt","a")
file.write("\n I am Learning Python")
file.close()

#Read Line by Line
file = open("data.txt","r")
for line in file:
    print(line)
    file.colse()