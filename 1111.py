import os
fileList_B = os.listdir('B')
os.chdir('B')
print(fileList_B)

f = open('b1.txt','r+')
f.seek(0,0)
print(f.read())