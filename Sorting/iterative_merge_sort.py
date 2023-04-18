def merge(arr, l,m,h):
    p1 = l
    p2 = m + 1
    temp = []
    temp.extend(arr[:l])

    
    while p1 <= m and p2 <= h:
        if arr[p1] > arr[p2]:
            temp.append(arr[p2])
            p2 += 1
        else:
            temp.append(arr[p1])
            p1 += 1

    while p1 <= m:
        temp.append(arr[p1])
        p1 += 1
    
    while p2 <= h:
        temp.append(arr[p2])
        p2 += 1


    temp.extend(arr[h+1:])
    return temp

def iter_merge_sort(arr):

    len_arr = len(arr)
    p = 2
    
    while p <= len_arr:
        for idx in range(0,len_arr + 1 - p ,p):
            low = idx
            high = idx + p - 1
            mid = (low + high)//2 
            arr = merge(arr,low,mid,high)
        if len_arr % p != 0:
            arr = merge(arr,idx + p,(idx + p + len_arr - 1)//2 ,len_arr -1 ) 
        p = p * 2

    if len_arr % p//2 != 0:
        arr = merge(arr,0,( len_arr - (len_arr % (p//2)) - 1)  ,len_arr -1 ) 

    return arr

print(iter_merge_sort([5,3,2,4,1,6,7]))