from merge_sort import merge_sort

def test_in_order():
    in_order_list = [1, 2, 3, 4, 5]
    actual = merge_sort(in_order_list)
    expected = [1, 2, 3, 4, 5]
    assert actual == expected


def test_descending_list():
    descending_order_list = [5, 4, 3, 2, 1]
    actual = merge_sort(descending_order_list)
    expected = [1, 2, 3, 4, 5]
    assert actual == expected


def test_duplicate_numbers():
    duplicates_list = [1, 2, 2, 4, 4, 2, 3, 3, 5]
    actual = merge_sort(duplicates_list)
    expected = [1, 2, 2, 2, 3, 3, 4, 4, 5]
    assert actual == expected


def test_negatives():
    negative_number_list = [-1, -2, -3, 4, 5]
    actual = merge_sort(negative_number_list)
    expected = [-3, -2, -1, 4, 5]
    assert actual == expected
