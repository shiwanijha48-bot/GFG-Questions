def pair_sum(arr, sum):
    # code here
    seen = {}
    for i in arr:
        rem = sum - i
        if rem in seen:
            return True
        seen[i] = 1
    return False
        
