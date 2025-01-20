'''file = open("Mytext.txt","+w")
file.write("Hello World ")
file.close()
file = open("Mytext.txt","r")
content = file.read()
print(content)
file.close()
file = open("Mytext.txt","a+")
file.write("\n Hi this is Anant Mishra \n  ")
file.seek(0)
content2 = file.read()
print(content2)
file.close()'''
''' Using write() & writelines()'''
'''file = open("Mytext.txt", "w")
file.close()
file = open("Mytext.txt","w")
s = (" Hello This is  your Boy Anant  \n" )
l =[ "And Welcome me with a huge round of applause \n let's make a cheers and invite him "]
file.write(s)
file.writelines(l)
file.seek(0)
content = file.read()
print(content)
file.close()'''

''' Using read() & readline() & readlines()'''
'''file = open("Mytext.txt", "r")
print(file.read())
file.seek(0)

print("first line ")
print(file.readline() , end = " ")
print("line second ")
print(file.readline() , end = " ")
file.seek(0)
print(file.readlines())
file.close()'''



