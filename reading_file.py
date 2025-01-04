#returns file wrapper
f = open('c:/Users/Fatoom/Documents/names.txt')
#print the file's content: read returns string
# print(f.read())
#print content of file using readLine
lines = [i for i in f.readlines()]
lines2 = []
for line in lines:
    lines2.append(line.strip())
print(lines2)