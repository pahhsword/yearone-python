# Gets the range between prices for three employees
def programmers(a, b, c):
    tbl = [a, b, c]
    tbl.sort()
    i_tbl_len = len(tbl)

    print(tbl[i_tbl_len - 1] - tbl[0])

programmers(147, 33, 526)
programmers(33, 72, 74)
programmers(1, 5, 9)
