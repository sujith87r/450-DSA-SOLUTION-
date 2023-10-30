# Python3 code for above approach
def duplicates(arr, n):
   
    # Increment array elements by 1
    for i in range(n):
        arr[i] = arr[i] + 1
         
    # result vector
    res = []
     
    # count variable for count of
    # largest element
    count = 0
    for i in range(n):
       
        # Calculate index value
        if(abs(arr[i]) > n):
            index = abs(arr[i])//(n+1)
        else:
            index = abs(arr[i])
             
        # Check if index equals largest element value
        if(index == n):
            count += 1
            continue
             
        # Get element value at index
        val = arr[index]
         
        # Check if element value is negative, positive
        # or greater than n
        if(val < 0):
            res.append(index-1)
            arr[index] = abs(arr[index]) * (n + 1)
        elif(val>n):
            continue
        else:
            arr[index] = -arr[index]
             
    # If largest element occurs more than once
    if(count > 1):
        res.append(n - 1)
    if(len(res) == 0):
        res.append(-1)
    else:
        res.sort()
    return res
   
# Driver Code
numRay = [ 0, 4, 3, 2, 7, 8, 2, 3, 1 ]
n = len(numRay)
ans = duplicates(numRay,n)
for i in ans:
    print(i)
