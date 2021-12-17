'''
* The most commonly used sorting algorithm
* Set a standard element and switch the element that is bigger than the standard with the element that is smaller than the standard
* The standard element is called PIVOT
* In Hoare Partition, the pivot is the first element
* Average Time Complexity: O(NlogN)
'''

# input example
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    if start >= end:  # stop if there is only 1 element
        return
    pivot = start # the first element is the pivot
    left = start + 1
    right = end
    while left <= right:
        # repeat until an element larger than the pivot is found
        while left <= end and array[left] <= array[pivot]:
            left += 1
        # repeat until an element smaller than the pivot is found
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right:  # if crossed, switch the small element with pivot
            array[right], array[pivot] = array[pivot], array[right]
        else: # if didn't cross, switch the small element with big element
            array[left], array[right] = array[right], array[left]
    # separately sort the left and the right part after the split
    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)

quick_sort(array, 0, len(array)-1)
print(array)
