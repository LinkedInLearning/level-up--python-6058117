def get_prime_factors(number):
    factors = []
    divisor = 2
    while divisor <= number:
        if number % divisor == 0:
            factors.append(divisor)
            number = number // divisor
        else:
            divisor += 1
    return factors

# 解决方案视频中使用的命令，仅供参考
# if __name__ == '__main__':
#     print(get_prime_factors(630))  # [2, 3, 3, 5, 7]
#     print(get_prime_factors(13))  # [13]

