import parsecases as pc



string_mat = list()
rotated_mat = list() 


for test_c in pc.parsed:
    string_mat.append(test_c)
    rotated_mat.append([0]*pc.size_mat)

pc.print_mat(string_mat)



base_max = pc.size_mat //2 



for base in range(base_max):
    
    row_ind = pc.size_mat - base - 1
    for col in range(base,pc.size_mat-base-1):
        string_mat[row_ind][base],string_mat[base][col] = string_mat[base][col], string_mat[row_ind][base]
        row_ind -= 1
 
    
    col_ind = base
    for row in range(base,pc.size_mat-base-1):
        string_mat[base][col_ind],string_mat[row][pc.size_mat-base-1] = string_mat[row][pc.size_mat-base-1], string_mat[base][col_ind]
        col_ind += 1
     
    row_ind = base
    for col in range(pc.size_mat-base-1,base,-1):
        string_mat[row_ind][pc.size_mat-base-1], string_mat[pc.size_mat-base-1][col] = string_mat[pc.size_mat-base-1][col],string_mat[row_ind][pc.size_mat-base-1]
        row_ind += 1
    

pc.print_mat(string_mat)