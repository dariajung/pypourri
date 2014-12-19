

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


if __name__ == "__main__":
    a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    # 1 2 3
    # 4 5 6
    # 7 8 9

    # 1 4 7
    # 2 5 8
    # 3 6 9

    assert(transpose(a)) == [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
    print "test passed"
