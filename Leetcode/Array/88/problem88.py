def merge(nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: None Do not return anything, modify nums1 in-place instead.
    """
    
    if(len(nums2) > 0):
        
        nums1Idx = m-1

        nums2Idx = n-1

        sortIdx = len(nums1)-1

        while(nums1Idx != -1 or nums2Idx != -1):
            if(nums2Idx == -1):
                nums1[sortIdx] = nums1[nums1Idx]
                sortIdx += -1
                nums1Idx  += -1

            elif(nums1Idx == -1):
                nums1[sortIdx] = nums2[nums2Idx]
                sortIdx += -1
                nums2Idx  += -1                

            elif(nums1[nums1Idx] >= nums2[nums2Idx]):
                nums1[sortIdx] = nums1[nums1Idx]
                sortIdx += -1
                nums1Idx  += -1

            elif(nums1[nums1Idx] < nums2[nums2Idx] ):
                nums1[sortIdx] = nums2[nums2Idx]
                sortIdx += -1
                nums2Idx  += -1
    print(nums1)
    return nums1

merge([1,2,3,0,0,0],3,[2,5,6],3)