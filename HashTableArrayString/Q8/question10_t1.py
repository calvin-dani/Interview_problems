import parsecases as pc

string_mat = list()
rotated_mat = list() 


for test_c in pc.parsed:
    string_mat.append(test_c)
    

pc.print_mat(string_mat)
rowSet = set()
colSet = set()

for listRow in range(len(string_mat)):
    for number in range(len(string_mat[listRow])):
        if string_mat[listRow][number] == 0:
            rowSet.add(listRow)
            colSet.add(number)

print(rowSet,colSet)
for rowIdx in rowSet:
    for colIdx in range(len(string_mat)):
        string_mat[rowIdx][colIdx] = 0

for colIdx in colSet:
    for rowIdx in range(len(string_mat[colIdx])):
        string_mat[rowIdx][colIdx] = 0


pc.print_mat(string_mat)
