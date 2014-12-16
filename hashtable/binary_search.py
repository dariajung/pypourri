# given a sorted list, implement binary search


def binary_search(array, value, l, u):

    search_complete = False

    lower = l
    upper = u

    while not search_complete:
        # upper and lower bounds

        mid = (lower + upper) / 2

        if value == array[mid]:
            search_complete = True
            return array[mid]
        elif lower == upper:
            # nothing found
            search_complete = True
            return None
        elif value < array[mid]:
            upper = mid - 1
        elif value > array[mid]:
            lower = mid + 1

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 7, 9, 10]

    # these should pass
    assert(binary_search(arr, 4, 0, len(arr) - 1)) == 4
    assert(binary_search(arr, 10, 0, len(arr) - 1)) == 10
    assert(binary_search(arr, 100, 0, len(arr) - 1)) is None
    assert(binary_search(arr, 5, 0, len(arr) - 1)) == 5
    assert(binary_search(arr, 6, 0, len(arr) - 1)) is None
    assert(binary_search(arr, 1, 0, len(arr) - 1)) == 1
    assert(binary_search(arr, -1, 0, len(arr) - 1)) is None
    print "yay all tests passed!"
