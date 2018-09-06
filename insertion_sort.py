def insertion_sort(l):
    for i in range(1, len(l)):
        key = l[i]
        j = i - 1
        while j >= 0 and l[j] > key:
            l[j + 1] = l[j]
            j = j - 1
        l[j + 1] = key
    return l

if __name__ == '__main__':
    print insertion_sort([8, 5, 4, 0, 7, 9, 1])