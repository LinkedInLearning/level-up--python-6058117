import secrets

def generate_passphrase(num_words, wordlist_path='diceware.wordlist.asc'):
    with open(wordlist_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()[2:7778]
        word_list = [line.split()[1] for line in lines]

    words = [secrets.choice(word_list) for i in range(num_words)]
    return ' '.join(words)


# 解决方案视频中使用的命令，仅供参考
# if __name__ == '__main__':
#     print(generate_passphrase(7))
#     print(generate_passphrase(7))
