m = int(input())
km = m/1000
if km < 0.1:
    VV = "00"

elif 0.1 <= km <= 5:
    if km < 1:
        VV = "0"+str(int(km*10))
    else:
        VV = int(km*10)

elif 6 <= km <= 30:
    VV = int(km+50)

elif 35 <= km <=70:
    VV = int((km-30)/5+80)

else:
    VV = 89
print(VV)
#ok
