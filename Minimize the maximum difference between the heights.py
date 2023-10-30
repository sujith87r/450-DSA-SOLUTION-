
# User function Template
def getMinDiff(arr, n, k):
    arr.sort()
    ans = arr[n - 1] - arr[0]  # Maximum possible height difference
 
    tempmin = arr[0]
    tempmax = arr[n - 1]
 
    for i in range(1, n):
        if arr[i] < k:
            continue
        tempmin = min(arr[0] + k, arr[i] - k)
 
        # Minimum element when we
        # add k to whole array
        # Maximum element when we
        tempmax = max(arr[i - 1] + k, arr[n - 1] - k)
 
        # subtract k from whole array
        ans = min(ans, tempmax - tempmin)
 
    return ans
 
 
# Driver Code Starts
k = 6
n = 6
arr = [7, 4, 8, 8, 8, 9]
ans = getMinDiff(arr, n, k)
print(ans)
 
