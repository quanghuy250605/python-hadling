

def thuat_toan(arr, start, end, x):
    if start > end:
        return 'not found'
    
    mid = (start + end) // 2
    
    if arr[mid] == x:
        return mid
    
    if arr[mid] < x:
        return thuat_toan(arr, mid + 1, end, x) 
    
    return thuat_toan(arr, start, mid - 1, x)  

arr = ["a", "b", "c", "d", "e", "f"]
x1 = thuat_toan(arr, 0, len(arr) - 1, "b")
print(x1)  