extfile = open("a_file.txt")
lines = textfile.readlines()
for line in reversed(lines):
    print(line)
    textfile.close()
