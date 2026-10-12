def binary_search(list: list[int], search_for: int):
    first_index = 0
    last_index = len(list) - 1
    while (first_index <= last_index):
        mid_index = (first_index + last_index) // 2
        mid_item = list[mid_index]

        # If the middle item is the requested item, we found the index
        if mid_item == search_for:
            return mid_index 

        # Middle item is smaller so we need to remove the bottom half
        elif mid_item < search_for:
            first_index = mid_index + 1

        # Middle item is bigger so we need to remove the top half
        else:
            last_index = mid_index - 1

    return -1

print(
    binary_search(
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21], 1
    )
)
