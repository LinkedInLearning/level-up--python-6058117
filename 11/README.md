# Python 代码挑战 #11：生成密码

你的目标是实现一个函数 `generate_passphrase()`，输入参数是密码中包含的单词数量，然后返回一个字符串，其中包含了从 [Diceware 列表](https://theworld.com/~reinhold/diceware.wordlist.asc) 中随机选择的单词序列，单词间使用空格。

```console
>>> generate_passphrase(4)
'correct horse battery staple'
```
