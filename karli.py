import csv

print("Hello world")

with open('example.csv', 'r') as t1, open('example2.csv', 'r') as t2:
    fileone = t1.readlines()
    filetwo = t2.readlines()

    for count,line in enumerate(filetwo):
        if line not in fileone:
           print("Line: ", count+1)
           print(line)

# with open('update.csv', 'w') as outFile:

#     for line in filetwo:
#         #for letter in line:
#         if line not in fileone:
#            print(line)
#            outFile.write(line)