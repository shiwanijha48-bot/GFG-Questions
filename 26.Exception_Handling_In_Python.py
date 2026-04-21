#User function Template for python3
def find_minimum(a, b):
    # Your code here 
    # Return the minimum of all the valid operations
    res = []
    res.append(a+b)
    res.append(a-b)
    res.append(a*b)
    try:
        res.append(a/b)
    except ZeroDivisionError:
        pass
    return int(min(res))
