# 競プロ（python）メモ

## Link

### 入力
* [Qiita: 競プロ等におけるpython3の標準入力](https://qiita.com/zenrshon/items/c4f3849552348b3dbe67)

### スニペット
* [Qiita: 競プロ界隈でpython強者がやっていることをまとめてみた](https://qiita.com/dekamisako/items/1c104e332351ab9389a6)

### ライブラリ
* [Qiita: Pythonで競プロやるときによく書くコードをまとめてみた（雑多なヒントがたくさん）](https://qiita.com/y-tsutsu/items/aa7e8e809d6ac167d6a1)
* [Qiita: Pythonで競プロをやる時にそこそこ使う書き方（itertools編）](https://qiita.com/uni745e/items/9823ce5cd9c279a12d8a)


### その他（To Read）
* [Qiita: ソートを極める！ 〜 なぜソートを学ぶのか 〜（けんちょん、ソート一覧）](https://qiita.com/drken/items/44c60118ab3703f7727f)
* [Youtube: 15 Sorting Algorithms in 6 Minutes（ソート一覧）](https://www.youtube.com/watch?v=kPRA0W1kECg)
* [Qiita: アルゴリズムとは何か！？ ～ 文系理系問わず楽しめる精選 6 問 ～（けんちょん）](https://qiita.com/drken/items/f909b79ee03e679c7142)
* [Qiita: 特集！知らないと損をする計算量の話（けんちょん、計算量）](https://qiita.com/drken/items/18b3b3db5735241465ef)
* [Qiita: Pythonistaなら知らないと恥ずかしい計算量のはなし（Pythonライブラリの計算量）](https://qiita.com/Hironsan/items/68161ee16b1c9d7b25fb)

### その他（Have Read）
* [Qiita: PythonでAtCoder青になるまで -Pythonで競プロやるときに気をつけること-](https://qiita.com/Kentaro_okumura/items/a6917572756a2e3c0da9)
* [Qiita: （関数の処理速度比較）](https://www.kumilog.net/entry/python-speed-comp#input-と-sysstdinreadline)
* [Hatena: Python で AtCoder を遊ぶときに知ってると便利かもしれないこと（雑多なヒント）](https://nagiss.hateblo.jp/entry/2019/03/12/012944)
* [Qiita: Pythonで使う競技プログラミング用チートシート（雑多なヒント）](https://qiita.com/_-_-_-_-_/items/34f933adc7be875e61d0)
* [Strassenアルゴリズム: 行列計算の高速化](https://en.wikipedia.org/wiki/Strassen_algorithm)



## random notes
### bisect
```
# import bisect
A = [1, 2, 3, 3, 3, 4, 4, 6, 6, 6, 6]
X = 3
var1 = bisect.bisect_left(A, X) # var1 = 2  # X未満の要素の個数
var2 = bisect.bisect_right(A, X) # var2 = 5  # X以下の要素の個数
```

### counter
* [counter 使い方](https://note.nkmk.me/python-collections-counter/)
```
lst = [11, 11, 12, 13, 13, 13]
a = Counter(lst).items()
# [(11, 2), (12, 1), (13, 3)]
```

### 3の倍数の個数をカウント
```
count = len([x for x in data if x % 3 == 0])
```

### 配列の転置
```
# 転置配列
transpose = [x for x in zip(*lst)]
# 列ごとの和
sum_row = [sum(x) for x in zip(*lst)] 
```

### 2次元配列を1次元に直す
```
lst_flatten = list(chain.from_iterable(lst))
```

### 文字列定数
```
import string
print(string.ascii_lowercase)
# abcdefghijklmnopqrstuvwxyz
# lst(string.ascii_lowercase) --> ['a', ..., 'z']
print(string.ascii_uppercase)
# ABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.ascii_letters)
# abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.digits)
# 0123456789
print(string.hexdigits)
# 0123456789abcdefABCDEF
```

### groupby
```
a = [1, 1, 2, 3, 3, 3, 1, 2, 2]

## 隣接する同じ値をまとめる
for key, value in itertools.groupby(a):
    print(key, list(value))
# 1 [1, 1]
# 2 [2]
# 3 [3, 3, 3]
# 1 [1]
# 2 [2, 2]

## 隣接する偶奇をまとめる
for key, value in itertools.groupby(a, key=lambda x: x % 2):
    print(key, list(value))
# 1 [1, 1]
# 0 [2]
# 1 [3, 3, 3, 1]
# 0 [2, 2]
```

### メモ化
メモ化を利用したい関数の前につけておく
```
@lru_cache(maxsize=None)
```

### stdinをファイルに置き換える
```
# 冒頭に追加しておく
stdin = open('sample.txt') 
```
