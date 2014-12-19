

# slowwww O(N^2)
def transpose(arr):
    new_mat = []
    row_i = 0

    for row in arr:
        new_row = []
        for c_i, col in enumerate(row):
            new_row.append(arr[c_i][row_i])

        new_mat.append(new_row)
        row_i += 1

    return new_mat


def rotate_90(arr):
    new_mat = transpose(arr)
    for row in new_mat:
        last = len(row) - 1
        row[0], row[last] = row[last], row[0]

    return new_mat


if __name__ == "__main__":
    a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    # 1 2 3
    # 4 5 6
    # 7 8 9

    # transposed
    # 1 4 7
    # 2 5 8
    # 3 6 9

    # rotated 90 deg
    # 7 4 1
    # 8 5 2
    # 9 6 3

    assert(transpose(a)) == [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
    assert(rotate_90(a)) == [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
    print "test passed"
