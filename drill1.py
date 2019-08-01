import os

# join files for absolute path
fName = 'PythonDrill1'

fPath = 'C:\\'

abPath = os.path.join(fPath, fName)
# open file
dirs = os.listdir(abPath)

# print files in directory with timestamp and end with .txt
time = os.path.getmtime(abPath)
for file in dirs:
    if file.endswith('.txt'):
        print(file,time)







