def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        # If the target is found, return the mid index.
        if array[mid] == target:
            return mid
        # If the value of the mid index is greater than the target, search the left part.
        elif array[mid] > target:
            end = mid - 1
        # If the value of the mid index is smaller than the target, search the right part.
        else:
            start = mid + 1
    return None
  
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
