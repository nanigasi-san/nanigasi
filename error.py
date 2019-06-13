def make_bbb(number):
    long = 10
    b_n = bin(number)[2:]
    bbb = "0"*(long-len(b_n))+b_n
    return bbb
print(make_bbb(5))