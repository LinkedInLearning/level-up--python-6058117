import re
import collections


def count_words(path):
    with open(path, 'r', encoding='utf-8') as file:
        all_words = re.findall(r"[0-9a-zA-Z-']+", file.read())
        all_words = [word.upper() for word in all_words]
        print(f'\n单词总数: {len(all_words)}')

        word_counts = collections.Counter(all_words)

        print('\n出现频率最高的前 20 个单词：')
        for word in word_counts.most_common(20):
            print(f'{word[0]}\t{word[1]}')


# 解决方案视频中使用的命令，仅供参考
# if __name__ == '__main__':
#     count_words('shakespeare.txt')
