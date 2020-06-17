# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here
    i = 0
    j = 0
    k = 0
    while len(arrA) > 0 and len(arrB) > 0:
        if arrA[i] < arrB[j]:
            merged_arr[k] = arrA[i]
            k = k + 1
            i = i + 1
        else:
            merged_arr[k] = arrB[j]
            k = k + 1
            j = j + 1

    while 0 < len(arrA):
        merged_arr[k] = arrA[i]
        k = k + 1
        i = i + 1

    while 0 < len(arrB):
        merged_arr[k] = arrA[j]
        k = k + 1
        j = j + 1

    print(merged_arr)

# TO-DO: implement the Merge Sort function below recursively


arrA = [5, 7, 9, 11, 13]
arrB = [2, 6, 10, 12, 15]
merge(arrA, arrB)


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
