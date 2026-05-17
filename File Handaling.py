# File Handaling
#Read a file

file = open("data.txt","r")
content = file.read()
print(content)
file.close()

#write a File
file = open("data.txt","w")
file.write("This is a new line")
file.close()