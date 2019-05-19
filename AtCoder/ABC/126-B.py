S = input()
up_y_flg = False
dw_y_flg = False
up_m_flg = False
dw_m_flg = False

if 1 <= int(S[0:2]) <= 12:
    up_m_flg = True
if 0 <= int(S[0:2]) <= 99:
    up_y_flg = True
if 1 <= int(S[2:4]) <= 12:
    dw_m_flg = True
if 0 <= int(S[2:4]) <= 99:
    dw_y_flg = True


if up_y_flg and dw_m_flg:
    if up_m_flg and dw_y_flg:
        print("AMBIGUOUS")
    else:
        print("YYMM")
elif up_m_flg and dw_y_flg:
    print("MMYY")
else:
    print("NA")