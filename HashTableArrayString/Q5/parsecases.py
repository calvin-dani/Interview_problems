fhand = open("C:/Users/calvi/OneDrive/Documents/Documents/CrackingInterviewProb/HashTableArrayString/Q5/testcasesstring.txt")

unparse = fhand.readlines()
to_parse = list()
parsed = list()

for line in unparse:
    if line != '\n':
        parsed.append(line.split())


