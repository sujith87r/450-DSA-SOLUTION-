# Function to find the intersection of two arrays
def find_intersection(arr1, arr2):
    set1 = set(arr1)
 
    # Removing duplicates from the first array
    result = []
 
    # Avoiding duplicates and adding intersections
    for num in arr2:
        if num in set1:
            result.append(num)
            set1.remove(num)
 
    return result
 
# Driver code
if __name__ == "__main__":
    arr1 = [1, 2, 4, 5, 6]
    arr2 = [2, 3, 5, 7]
 
    # Function call
    intersection = find_intersection(arr1, arr2)
    for num in intersection:
        print(num, end=" ")
