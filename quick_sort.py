def swap(A, index1, index2):
    temp = A[index1]
    A[index1] = A[index2]
    A[index2] = temp

def partition(A, left, right):
    pivot = right - 1
    split = left - 1
    for j in range(left, right-1):
        if A[j] <= A[pivot]:
            swap(A, j, split + 1)
            split = split + 1
    swap(A, pivot, split + 1)
    return split + 1

def quick_sort(A, left, right):
    """

    in-place algorithm

    :param A: list of items
    :param left: left most index
    :param right: right most index
    :return:

        Correctness: induction
            - claim: left <= j <= right - 1
            - all items A[left, split] are <= pivot
            - all items A[split+1, right] are > pivot
        Time:
            - O(n log n) best case
            - O(n^2) worst case
    """
    # A is never empty
    if left < right:
        split = partition(A, left, right)
        quick_sort(A, left, split - 1)
        quick_sort(A, split + 1, right)
    return A


if __name__ == '__main__':
    A = [8, 5, 4, 0, 7, 9, 1]
    print quick_sort(A, 0, len(A))