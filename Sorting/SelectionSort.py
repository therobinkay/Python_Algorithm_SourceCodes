# input example
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i # index of the smallest element
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i] # swap

print(array)

'''
* Select the smallest element and swap it with the first element, and select the second smallest and swap it with the second, repeat
* Inefficient Time Complexity: O(N^2)
'''
