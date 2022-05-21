from insertion_sort.insertion_sort import insertion_sort

list_a = [5, 7, 3]
list_b = [53, 42, 12]
list_c = [2, 7, 34, 5, 7, 578, 52, 34, 2, 234, 5, 4, 6, 467, 8, 69, 8, 9, 45, 645, 64, 3, 45, 345, 9]


def test_insertion_sort_exists():
    assert insertion_sort


def test_sort_mixed_order():
    actual = insertion_sort(list_a)
    expected = [3, 5, 7]
    assert actual == expected


def test_sort_descending_order():
    actual = insertion_sort(list_b)
    expected = [12, 42, 53]
    assert actual == expected


def test_insertion_sort_large():
    actual = insertion_sort(list_c)
    expected = [2, 2, 3, 4, 5, 5, 6, 7, 7, 8, 8, 9, 9, 34, 34, 45, 45, 52, 64, 69, 234, 345, 467, 578, 645]
    assert actual == expected
