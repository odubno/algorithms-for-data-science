

def merge(A, left, mid, right):
    L = A[left:mid]
    R = A[mid:right]
    i, j = 0, 0
    k = left
    for l in range(k, right):
        if j >= len(R) or (i < len(L) and L[i] < R[j]):
            A[l] = L[i]
            i = i + 1
        else:
            A[l] = R[j]
            j = j + 1


def merge_sort(A, left, right):
    if right - left > 1:
        mid = int((left + right) / 2)
        merge_sort(A, left, mid)
        merge_sort(A, mid, right)
        merge(A, left, mid, right)

if __name__ == '__main__':
    A = [3, 6, 7, 2, 5, 1, 9]
    print A
    merge_sort(A, 0, len(A))
    print A