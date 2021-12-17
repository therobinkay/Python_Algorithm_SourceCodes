# input example
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    for j in range(i, 0, -1): # repeat as index i reduces to 1
        if array[j] < array[j-1]: # move to one left
            array[j], array[j-1] = array[j-1], array[j]
        else: # stop when meets a smaller element
            break

print(array)

'''
- Check each data and insert it at an appropriate place
- More efficient than Selection Sort: O(N)~O(N^2)
- Way more efficient when the data is already almost sorted
'''
