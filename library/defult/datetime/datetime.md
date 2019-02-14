## datetimeモジュールの使い方(2019/2/14)
### datetimeモジュール：日付や時間などを求めることが出来るライブラリ
| datetimeを使って出来ること|
|:-:|
|一定時間ごとに動作するプログラムを書く|
|タイムスタンプを押す|
---
## datetimeモジュールの基本
### datetime型


|オブジェクトの生成|インスタンス|
|:-|:-|
|特定の日時を指定する|datetime()|
|現在の年/月/日/時間(24h)を取得する|datetime.now()|
|UNIXエポックのタイムスタンプをdatetime型に変換する|datetime.fromtimestamp()|

|要素|属性|
|:-|:-|
|年|year|
|月|month|
|日|day|
|時|hour|
|分|minute|
|秒|second|

|役割|メソッド|
|:-|:-|
|datetimeオブジェクトを文字列に変換する|.strftime(format)<div>※strftimeのフォーマットについては後述する。|
|文字列をdatetimeオブジェクトに変換する|.strptime(parse)|

### sample codes
> **特定の日時を指定する**
```Python
from datetime import*
birth_day = datetime(1996,2,12,15,23,52) #生まれた日時
print(birth_day.day) #生まれた日付
```

> **現在日時を取得する**
```Python
from datetime import*
now = datetime.now()
print(now.year) #現在の年
print(now.hour,now.minute,now.second) #現在の日時
```

> **UNIXエポックの利用**
```python
from datetime import*
import time
after_million = datetime.fromtimestamp(1000000)
print(after_million) #UNIXエポックの1000000秒後
now = datetime.fromtimestamp(time.time())
print(now) #timeモジュールの応用
```

---

#### strftimeのフォーマット
|format|意味|例|
|:-:|:-|:-:|
|%Y|4桁の西暦|"2019"|
|%y|西暦の下2桁|"00"~"99"|
|%m|10進数による月|"01"~"12"|
|%B|月名|"November"|
|%b|月の略称|"Nov"|
|%d|日にち|"01"~"31"|
|%j|年初からの日数|"001"~"336"|
|%w|曜日の数字|"0"(日)~"6"(土)|
|%A|曜日名|"Monday"|
|%a|曜日の略称|"Mon"|
|%H|時(24)|"00"~"23"|
|%I|時(12)|"01"~"12"|
|%M|分|"00"~"59"|
|%S|秒|"00"~"59"|
|%p|午前・午後|"AM","PM"|

### sample codes
> **datetimeオブジェクトから文字列を抽出する**
```python
from datetime import*
oct21st = datetime(2019,10,21,3,34,0)
print(oct21st.strftime("%Y/%m/%d %H:%M:%S"))
print(oct21st.strftime("%H%Mな阪関"))
```

> **文字列をdatetimeオブジェクトに変換する**
```Python
from datetime import*
today = datetime.strptime("February 14, 2019","%B %d, %Y")
print(today)
```
