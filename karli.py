import csv

print("Hello world")

with open('example.csv', 'r') as t1, open('example2.csv', 'r') as t2:
    fileone = t1.readlines()
    filetwo = t2.readlines()

with open('update.csv', 'w') as outFile:
    for line in filetwo:
        for letter in line:
            print(letter)
        #if line not in fileone:
        #    outFile.write(line)