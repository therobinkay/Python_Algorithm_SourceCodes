'''
* Extremely fast but only works under certain conditions
* Only works for integer data, efficient when the range is less than 1mil
* Sort by memorizing sorting information
* Time/Space Complexity: O(N+max(data))
* If difficult to define the characteristics of the dataset, use quick sort!
'''

# assume all elements are greater than or equal to 0
array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
# define a list that covers the entire range (set every value to 0)
count = [0] * (max(array) + 1)

for i in range(len(array)):
    count[array[i]] += 1  # increase the index of each data

for i in range(len(count)): # check the sorted info from the list
    for j in range(count[i]):
        print(i, end=' ') # print the indices, distinguished by a space
