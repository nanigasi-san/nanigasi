def main():
    import sys
    input = sys.stdin.readline
    import numpy as np
    from itertools import accumulate
    all_num = 0

    N,K = map(int,input().split())
    input_list = list(map(int,input().split()))
    a_array = np.array(input_list)
    ruisekiwa = np.array(list(accumulate(input_list)))
    for _ in range(N):
        for i,ruiseki in enumerate(ruisekiwa[_:],_):
            if ruiseki >= K:
                all_num += N-i
                ruisekiwa -= a_array[_]
                break
    print(all_num)
if __name__ == "__main__":
    main()