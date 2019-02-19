## Fortranのススメ
#### 某

---

### **Fortran**とは？
***古の古代魔法(ダブルミーニング)***
+ 科学計算などに使われているプログラミング言語 |

---

### Fortranの特徴
+ 実行が速い性的言語 |
+ 非プログラマ(研究者)向けなので書きやすい |
+ 強そう |

---

```fortran

implicit none
INTEGER :: n,i,j,count,challenge_divide
INTEGER,ALLOCATABLE,DIMENSION(:) :: a

READ(5,*) n
ALLOCATE(a(n))
READ(5,*) (a(i),i=1,n)

count = 0

do j=1,1000
    challenge_divide = 0

    do i=1,n
        if (MOD(a(i),2)==0) then
            challenge_divide = challenge_divide+1
        endif
    enddo

    if (challenge_divide==n) then
        count = count+1
        do i=1,n
            a(i) = a(i)/2
        enddo
    else
        exit
    endif
enddo

WRITE(6,*) count

end

```

---

終わり💛
---
