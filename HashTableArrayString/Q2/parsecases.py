fhand = open("testcasesstring.txt")

unparse = fhand.readlines()
to_parse = list()
parsed = list()

for line in unparse:
    if line != '\n':
        parsed.append(line.strip())


  
