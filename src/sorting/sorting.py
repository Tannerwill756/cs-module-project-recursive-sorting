# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here
    # start pointers at the start of both lists
    a, b = 0, 0

    # loop through our merged_arr
    for i in range(len(merged_arr)):
        # compare the values at both pointers
        # whichever value is smaller we copy that value to our merged list
        # increment that pointer
        # check fi a pointer is out of bounds of its respective array
        # if it is, then we copy over every element form the other array
        if a >= len(arrA):
            merged_arr[i] = arrB[b]
            b += 1
        elif b >= len(arrB):
            merged_arr[i] = arrA[a]
            a += 1

        # both indices are still in bounds of their respective arrays
        elif arrA[a] < arrB[b]:
            merged_arr[i] = arrA[a]
            a += 1
        else:
            merged_arr[i] = arrB[b]
            b += 1

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively


# arrA = [5, 7, 9, 11, 13]
# arrB = [2, 6, 10, 12, 15]
# merge(arrA, arrB)


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


# scary_Array = [6, 7, 5, 2, 1, 15, 13, 10]
# merge_sort(scary_Array)

# STRETCH: implement the recursive logic for merge sort in a way that doesn't
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists
# or data structures; it can only re-use the memory it was given as input


# def merge_in_place(arr, start, mid, end):
#     # Your code here


# def merge_sort_in_place(arr, l, r):
#     # Your code here
