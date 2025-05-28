import time
import random

def waiting_game():
    """
    一个等待游戏，目标是尽可能接近指定的时间间隔。
    """
    target = random.randint(2, 4)  # 目标等待时间（秒）
    print(f'\n你的目标时间是 {target} 秒')

    input(' --- 按 Enter 键开始 --- ')
    start = time.perf_counter()

    input(f'\n...等待 {target} 秒后再次按 Enter 键...')
    elapsed = time.perf_counter() - start

    print(f'\n经过时间：{elapsed :.3f} 秒')
    if elapsed == target:
        print('(完美！)')
    elif elapsed < target:
        print(f'（快了 {target - elapsed :.3f} 秒）')
    else:
        print(f'（慢了 {elapsed - target :.3f} 秒）')


# if __name__ == '__main__':
#     waiting_game()
