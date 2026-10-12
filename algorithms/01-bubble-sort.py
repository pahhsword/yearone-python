# Bubble Sort Algorithm


# Bubble sort Algo
def bubble_sort(l):
    list_len = len(l)
    index_len = list_len - 1

    # While list length is bigger than 1 so iterate until fully sorted
    while list_len > 0:

        # For that goes throguh each item in the list
        for i in range(0, index_len):

            # Compare the first value to the second
            if l[i] > l[i + 1]:

                # Switch the two values
                switch = l[i]
                l[i] = l[i + 1]
                l[i + 1] = switch

        # Reduce the iteration count so it does not loop infinitely
        list_len = list_len - 1

    print("Full list ->", l)


bubble_sort([23, 25, 67, 128, 12, 10, 13, 0])
