# function to find the maximum number of cuts
def maximize_cuts(n, x, y, z):
    # if the rod length is 0, no more cuts can be made
    if n == 0:
        return 0
    # if the rod length becomes negative, return negative infinity
    if n < 0:
        return float('-inf')
 
    # Calculate the number of cuts using each possible cut length (x, y, z)
    a = maximize_cuts(n - x, x, y, z) + 1
    b = maximize_cuts(n - y, x, y, z) + 1
    c = maximize_cuts(n - z, x, y, z) + 1
 
    # Find the maximum number of cuts among the three possibilities
    d = max(a, max(b, c))
    return d
 
if __name__ == "__main__":
    l = 11
    p = 2
    q = 3
    r = 5
 
    # Call the maximize_cuts function and print the result
    print(maximize_cuts(l, p, q, r))
