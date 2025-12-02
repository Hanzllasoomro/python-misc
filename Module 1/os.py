import os

os.getcwd()
os.listdir() #specific path - ("c:\\)
if(os.path.exists("d:\\")):
    os.chdir("d:\\")
    os.makedirs("d:\\python\\")
    os.getcwd()
else:
    print("Path doesn't exist")
