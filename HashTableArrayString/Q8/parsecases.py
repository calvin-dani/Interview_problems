fhand = open("testcasesmatrix.txt")


size_mat = None


unparse = fhand.readlines()
to_parse = list()
parsed = list()
index = 0

for line in unparse:
    temp = list()
    if size_mat == None:
        size_mat = int(line.strip())
    elif line != "\n":
        for number in line.strip().split():
            temp.append(int(number))
        parsed.append(temp)

        index += 1


def print_mat(print_lists):
    for line in print_lists:
        print(line)
