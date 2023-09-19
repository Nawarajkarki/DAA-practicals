def selectionSort(arr, n) -> list:
    for i in range(n-1):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[min_idx], arr[i] =  arr[i], arr[min_idx],

    return arr


def main():
    my_list=[5,8,7,4,2,9,12,13,11]
    n = len(my_list)

    # Make a copy of the original unsorted list
    unsorted_list = my_list.copy()

    Sorted_list = selectionSort(my_list, n)
    print(f"UnSorted list/Array {unsorted_list}")
    print(f"Sorted list/Array   {Sorted_list}")


if __name__ == '__main__':
    main()