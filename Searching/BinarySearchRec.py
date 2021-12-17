def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end)//2
    # return mid index if the target is found
    if array[mid] == target:
        return mid
    # check the left if the target is smaller than mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    # check the right if the target is larger than mid
    else:
        return binary_search(array, target, mid+1, end)
    
# input the number of elements(n) and the desired string(target)
n, target = list(map(int, input().split()))
# input the entire elements
array = list(map(int, input().split()))

# return the binary search
result = binary_search(array, target, 0, n-1)
if result == None:
    print("The element does not exist.")
else:
    print(result + 1)
