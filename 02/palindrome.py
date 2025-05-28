import re

def is_palindrome(phrase):
    forwards = ''.join(re.findall(r'[a-z]+', phrase.lower()))
    backwards = forwards[::-1]
    return forwards == backwards


# 解决方案视频中使用的命令，仅供参考
# if __name__ == '__main__':
#     print(is_palindrome('hello world'))  # false
#     print(is_palindrome("Go hang a salami, I'm a lasagna hog."))  # true
