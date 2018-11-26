A = int(input())
B = int(input())
C = int(input())
X = int(input())
def main(A,B,C,X):
    num = 0
    for a in range(A+1):
        A_ = 500*a
        for b in range(B+1):
            B_ = 100*b
            for c in range(C+1):
                C_ = 50*c
                if A_ + B_ + C_ == X:
                    num += 1
                    continue

    print(num)
main(A,B,C,X)
