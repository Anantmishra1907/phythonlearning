''' this is a program where read a file line by line and  store it into list '''
def readfiletotest(filename):
  lines = []
  with open ("Mytext.txt", "r") as file :
    while True :
      line = file.readline()
      if not line :
        break 
      lines.append(line.strip())
  return lines 
filename = "Mytext.txt"
a = readfiletotest(filename)
print(a)
 

