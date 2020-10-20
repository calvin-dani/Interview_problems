fhand = open("C:/Users/calvi/OneDrive/Documents/Documents/CrackingInterviewProb/HashTableArrayString/testcasesarray.txt")

unparse = fhand.readlines()
to_parse = list()
parsed = list()

for line in unparse:
    if line != '\n':
        to_parse.append(line.split())
    
for item_num in range(len(to_parse)):
    parsed.append([])
    for num in range(len(to_parse[item_num])):
        parsed[item_num].append(int(to_parse[item_num][num]))


  
