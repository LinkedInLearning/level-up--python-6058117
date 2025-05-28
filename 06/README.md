# Python 代码挑战 #6: 保存字典

你的目标是实现两个函数，`save_dict()` 和 `load_dict()`。 

`save_dict()` 函数有两个参数：要保存的字典对象和保存的文件路径。 它会将字典对象保存到指定的文件中。 

`load_dict()` 函数有一个参数：字典文件的路径，它会从文件中加载保存的字典对象。

## 示例测试输出
```console
>>> save_dict({1: 'a', 2: 'b', 3: 'c'}, 'test.pickle')
>>> print(load_dict('test.pickle'))
{1: 'a', 2: 'b', 3: 'c'}
```
