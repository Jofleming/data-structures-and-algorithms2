def merge_sort(lst):

    n = len(lst)
    print(f'Sorting {lst} via merge method')

    if n > 1:
        mid = n // 2
        left = lst[:mid]
        right = lst[mid:]

        print(f'Splitting into left: {left} and right: {right}')

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                lst[k] = left[i]
                print(f'{left[i]} is smaller than {right[j]} so we will add that to the next value in the list giving us {lst}')
                i += 1
            else:
                lst[k] = right[j]
                print(f'{right[j]} is smaller than {left[i]} so we will add that to the next value in the list giving us {lst}')
                j += 1
            k += 1
        if i == len(left):
            print('We have now finished with left. Time to add the rest of right')
            while j< len(right):
                lst[k] = right[j]
                k += 1
                j += 1
        else:
            print('We have finished with left now we need to add the rest of right')
            while i < len(left):
                lst[k] = left[i]
                k += 1
                i += 1
        print(f'Sorted list: {lst}')
    return lst


if __name__ == "__main__":
    test_lst = [8,2,32,48]
    merge_sort(test_lst)