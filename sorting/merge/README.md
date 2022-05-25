# Blog Notes: Merge Sort

Merg sort is the act of splitting a list into easily sortable sizes and then putting them in the correct order as you build back up.

## How it works

1. With a given list you will find the mid point
2. Using the mid point split the list into a left and right half
3. Recursively repeat until each left and right is only one entry
4. Merge the individual pieces back together using comparisons to sort correctly
5. Take care of any remainder on a side by adding on it at the end.

## Psuedocode

```
ALGORITHM Mergesort(arr)
    DECLARE n <-- arr.length

    if n > 1
      DECLARE mid <-- n/2
      DECLARE left <-- arr[0...mid]
      DECLARE right <-- arr[mid...n]
      // sort the left side
      Mergesort(left)
      // sort the right side
      Mergesort(right)
      // merge the sorted left and right sides together
      Merge(left, right, arr)

ALGORITHM Merge(left, right, arr)
    DECLARE i <-- 0
    DECLARE j <-- 0
    DECLARE k <-- 0

    while i < left.length && j < right.length
        if left[i] <= right[j]
            arr[k] <-- left[i]
            i <-- i + 1
        else
            arr[k] <-- right[j]
            j <-- j + 1

        k <-- k + 1

    if i = left.length
       set remaining entries in arr to remaining values in right
    else
       set remaining entries in arr to remaining values in left
```

## Code

```
def merge_sort(lst):

    n = len(lst)

    if n > 1:
        mid = n // 2
        left = lst[:mid]
        right = lst[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                lst[k] = left[i]
                i += 1
            else:
                lst[k] = right[j]
                j += 1
            k += 1
        if i == len(left):
            while j< len(right):
                lst[k] = right[j]
                k += 1
                j += 1
        else:
            while i < len(left):
                lst[k] = left[i]
                k += 1
                i += 1
    return lst
```

## Walkthrough

Step 1:<br/>
Sorting [8, 2, 32, 48] via merge method<br/>
Given the above list we have a length of 4 and will split into two groups of two.

Step 2:<br/>
Splitting into left: [8, 2] and right: [32, 48]<br/>
We keep recursively calling until we have a length of 1. It goes down the left side first.

Step 3:<br/>
Sorting [8, 2] via merge method<br/>
Splitting into left: [8] and right: [2]<br/>
Sorting [8] via merge method<br/>
Sorting [2] via merge method<br/>
2 is smaller than 8 so we will add that first. We then add 8 as the next value in the list giving us [2, 8]<br/>
Sorted list: [2, 8]<br/>
We have finished with left now we need to add the rest of right

Step 4:<br/>
This will look very similar as above. Splitting the right side again down to length 1 lists.<br/>
Sorting [32, 48] via merge method<br/>
Splitting into left: [32] and right: [48]

Step 5<br/>
This is where we start building back up the right side. Nothing should change since this part of our original list was in order.<br/>
Sorting [32] via merge method<br/>
Sorting [48] via merge method<br/>
32 is smaller than 48 so we will add that to the next value in the list giving us [32, 48]<br/>
Sorted list: [32, 48]

Step 6<br/>
Now it is time to bring the two halves together. We compare the first index of the two sorted halves as those will be the lowest numbers. We then add whichever is lower to the final list and repeat.

2 is smaller than 32 so we will add that to the next value in the list giving us [2,]<br/>
8 is smaller than 32 so we will add that to the next value in the list giving us [2, 8,]<br/>
Since the left list is empty we will just append the right list.<br/>
Sorted list: [2, 8, 32, 48]

As you can see our list is now sorted! Congratulations!

### Big O

Time: O(log(n))
    This is because as the function itself gets larger it is not linear. The act of splitting it is log(n) and the act of building it back up is just n. Since you drop the constant it simplifies to log(n).

Space: O(n)
    This is because we are given the one list as an input. From there how many sub lists we make is linear based off of that.
