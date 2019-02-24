year,month,day = input().split("/")
#1 =平成
year = int(year)
month = int(month)
day = int(day)
flg = 0
if year<=2019:
    if year == 2019:
        if month<=4 and day <=30:
            flg = 1
    else:
        flg = 1

else:
    pass

if flg==1:
    print("Heisei")
else:
    print("TBD")
