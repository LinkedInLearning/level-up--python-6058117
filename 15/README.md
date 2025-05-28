# Python 代码挑战 #15：下载文件序列

你的目标是实现一个函数 `download_files()`，它接受两个输入参数：文件序列中第一个文件的 URL，以及文件的保存路径。

## 示例测试输出
我们将使用包含 50 张图片的示例 URL，第一张图片位于 http://699340.youcanlearnit.net/image001.jpg：

```console
>>> download_files('http://699340.youcanlearnit.net/image001.jpg', './images')
成功下载 image001.jpg
成功下载 image002.jpg
成功下载 image003.jpg
成功下载 image004.jpg
成功下载 image005.jpg
成功下载 image006.jpg
成功下载 image007.jpg
成功下载 image008.jpg
成功下载 image009.jpg
成功下载 image010.jpg
成功下载 image011.jpg
成功下载 image012.jpg
成功下载 image013.jpg
成功下载 image014.jpg
成功下载 image015.jpg
成功下载 image016.jpg
...
```
