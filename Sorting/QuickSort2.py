# input example
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array):
    # stop if the number of element is less than or equal to 1
    if len(array) <= 1:
        return array

    pivot = array[0]  # pivot is the first element
    tail = array[1:]  # list without pivot

    left_side = [x for x in tail if x <= pivot] # left part after the split
    right_side = [x for x in tail if x > pivot] # right part after the split

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행하고, 전체 리스트를 변환
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))
