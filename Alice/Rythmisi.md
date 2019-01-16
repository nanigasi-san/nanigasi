# Module [**Rythmisi**](https://github.com/nanigasi-san/nanigasi/blob/master/Alice/Rythmisi.py)

+ ## class <<!---->Dimiourgia>
    + ### olokliro(self,object(=[]))
        引数のリストまたはタプル**object**を集合に変換したものを返す。
        引数がない場合は空集合を生成する。  

    + ### meros(self,super,constraint)
        引数の集合**super**の要素のうち、指定した制約条件を満たす要素の部分集合を返す。
        制約条件は要素を**x**として記述する。

    + ### sympliroma(self,super,sub)
        引数の集合**super**,**sub**<!---->より、**super**<!---->を全体集合とした**sub**の補集合を返す。
        要素がすべて同じ場合(super==sub)、空集合を返す。
    + ### kai(self,*args)
        任意の数の引数の集合全ての和集合を返す。

    + ### proion(self,\*args)
        任意の数の引数の集合全ての積集合を返す。

    + ### ekthetiki(self,set)
        引数の集合**set**の冪集合を返す。

---
|引数|型|
|:-:|:-:|
|**object**|list or tuple|
|**super**|sympy.sets.sets.FiniteSet|
|**sub**|sympy.sets.sets.FiniteSet|
|**set**|sympy.sets.sets.FiniteSet|
|**constraint**|sympy.core.relational.StrictGreaterThan|
|**\*args**|sympy.sets.sets.FiniteSet|
---
