file=open("file.txt","a+t")
file.seek(0)
content=file.read()
line=file.write("Hello World")
file.seek(0)
print(content)
file.close()