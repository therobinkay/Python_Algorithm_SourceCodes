def rotate_a_matrix_by_90_degree(a):
    n = len(a)  # number of rows
    m = len(a[0])   # number of cols
    result = [[0]*n for _ in range(m)]  # resulting list
    for i in range(n):
        for j in range(m):
            result[j][n-i-1] = a[i][j]
    return result
