testArray = [2,1,5,3,2]

def max_subarray_sum(array,k):
    maxSum = sum(array[0:2])
    for i in range(len(array)-(k-1)):
        pSum = sum(array[i:(i+k-1)])
        if pSum > maxSum:
            maxSum = pSum
    return maxSum

print(max_subarray_sum(testArray,3))