import os

# join files for absolute path
fName = 'PythonDrill1'

fPath = 'C:\\'

abPath = os.path.join(fPath, fName)
# open file
dirs = os.listdir(abPath)

# print files in directory
for file in dirs:
    print(file)

# print file with time stamp
time = os.path.getmtime(abPath)

for file in dirs:
    print(file,time)


