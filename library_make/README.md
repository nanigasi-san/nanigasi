# nanigasi_sequence 数列操作のためのライブラリ
---
## クラス構成
+ Sequence
  + ArithmeticalProgression
  + GeometricProgression
  + Zennka1
---
## クラスと引数の説明
#### `Sequence(self,general_term)`
単純な数列。一般項が判明している場合にはそのまま使える。
|引数|型|デフォルト値|
|:-|:-|:-|
|general_term(一般項)|str|

#### `ArithmeticalProgression(Sequence,first_term,ccommon_diff)`
等差数列。初項と公差が判明しているときにSequenceインスタンスを生成する。
|引数|型|デフォルト値|
|:-|:-|:-|
|first_term(初項)|float||
|common_diff(公差)|float||

#### `GeometricProgression(Sequence,first_term,ccommon_ratio)`
等比数列。初項と公比が判明しているときにSequenceインスタンスを生成する
|引数|型|デフォルト値|
|:-|:-|:-|
|first_term(初項)|float||
|common_ratio(公比)|float||

#### `Zennka1(Sequence,first_term,recurrence_fomula)`
数列。初項と一変数の漸化式が判明しているときに数列を生成する。
|引数|型|デフォルト値|
|:-|:-|:-|
|first_term(初項)|float||
|recurrence_fomula(漸化式)|str||

---
## methods
### Sequenceクラス共通
+ `Sequence.get_term(self,num)`:数列のnum項目の値を返す(num>=1)
+ `Sequence.enumeration(self,start,end)`:数列のstart項目からend項目までの数列のジェネレーターを返す
+ `Sequence.sigma(self,start,end)`:数列のstart項目からend項目までの数列の和を返す
### Zennka1クラス
+ `Zennka1.zenka(self,end)`:漸化数列のend項目までのリストを返す

---
## examples
#### インポート
```python
from nanigasi_sequence import Sequence,ArithmeticalProgression,GeometricProgression,Zennka1
```
#### 一般項が分かっている場合
```python
a = Sequence("n**2+3*n")

print(a.general_term)
# n**2 + 3*n

print(a.get_term[3])
# 18

print(a.enumeration(1,5))
# <generator object Sequence.enumeration.<locals>.<genexpr> at 0x000001D0A632FD68>

print(list(a.enumeration(4,8)))
# [28,40,54,70,88]

print(a.sigma(1,10))
# 550
```
---
#### 等差数列
```python
b = ArithmeticalProgression(3,2) #初項3,公差2の等差数列

print(b.general_term)
# 2*n + 1

for number in b.enumeration(1,10):
    print(number)
# 3
# 5
# 7
# 9
# 11
# 13
# 15
# 17
# 19
# 21

print(b.sigma(1,6))
# 48
```
---
#### 等比数列
```python
c = GeometricProgression(8,3) #初項8,公比3の等比数列

print(c.general_term)
# 8*3**(n - 1)

print(c.get_term(4))
# 216
```
---
#### 漸化数列
```python
d = Zennka1(-1,"2*a_n+n") #初項-1,漸化式a_n+1 = 2*a_n+nの数列

print(d.recurrence_fomula)
# 2*a_n + n

print(d.zenka(10))
# [-1,-1,0,3,10,25,56,119,246,501]
```
---
