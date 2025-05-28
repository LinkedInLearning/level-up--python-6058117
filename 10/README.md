# Python 代码挑战 #10：统计唯一单词

你的目标是实现一个名为 `count_words()` 的函数，该函数接收一个文本文件的路径作为输入参数，然后打印文件中单词总数，以及 20 个最常用的单词和每个单词出现的次数。

## 示例测试输出
使用 [莎士比亚全集](https://www.gutenberg.org/cache/epub/100/pg100.txt) 作为输入：

```console
>>> count_words('shakespeare.txt')


单词总数：976836

出现频率最高的前 20 个单词：
THE      30257
AND      28413
I        23070
TO       20997
OF       18824
A        16163
YOU      14570
MY       13179
IN       12333
THAT     12063
IS       9858
NOT      9066
WITH     8531
ME       8262
FOR      8244
IT       8212
HIS      7583
BE       7384
THIS     7165
HE       7100
```
