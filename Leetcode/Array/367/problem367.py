def isPerfectSquare(num):
    """
    :type num: int
    :rtype: bool
    """
    left = 0
    right = num
    while(left <= right):
        mid = (left + right)//2
        square = mid * mid
        if(square > num):
            right = mid-1
        elif(square < num):
            left = mid+1
        elif(square == num):
            return True
    return False
print(isPerfectSquare(1))