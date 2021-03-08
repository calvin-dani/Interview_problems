import parsecases as pc


string_mat = list()
rotated_mat = list()


for test_c in pc.parsed:
    string_mat.append(test_c)
    rotated_mat.append([0] * pc.size_mat)

pc.print_mat(string_mat)


row_ind = 0
col_ind = 0

for col in range(pc.size_mat):
    for row in range(pc.size_mat - 1, -1, -1):
        rotated_mat[row][col] = string_mat[row_ind][col_ind]
        col_ind += 1
    row_ind += 1
    col_ind = 0

pc.print_mat(rotated_mat)
