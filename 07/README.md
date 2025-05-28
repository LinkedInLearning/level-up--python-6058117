# Python 代码挑战 #7: 调度函数

你的目标是实现一个函数 `schedule_function()`，它有三个参数：运行函数的时间、要执行的函数名称，以及传递给调度函数的数量不固定的参数。

当你的 `schedule_function()` 被调用时，它应该立即打印一条消息，显示要调度的函数名称，以及执行的时间。

## 示例测试输出
```console
>>> schedule_function(time.time() + 1, print, '你好！')
print() 已安排在 2022 年 8 月 14 日 20:39:28 运行
```
一秒钟后...
```console
你好！
```
