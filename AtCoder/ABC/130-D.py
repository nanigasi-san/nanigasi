def main():
    import sys
    input = sys.stdin.readline
    
    N,K = map(int,input().split())
    atuple = tuple(map(int,input().split()))
    all_num = 0
    for _ in range(N):
        num = 0
        for i,a in enumerate(atuple[_:],_):
            num += a
            if num >= K:
                all_num += N-i
                break

    print(all_num)

if __name__ == "__main__":
    main()