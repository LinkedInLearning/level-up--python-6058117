def sort_words(words):
    return ' '.join(sorted(words.split(), key=str.casefold))

# 解决方案视频中使用的命令，仅供参考
# if __name__ == '__main__':
#     print(sort_words('banana ORANGE apple'))  # apple banana ORANGE
