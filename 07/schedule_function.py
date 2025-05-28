import sched
import time

def schedule_function(event_time, function, *args):
    s = sched.scheduler(time.time, time.sleep)
    s.enterabs(event_time, 1, function, argument=args)
    print(f'{function.__name__}() 计划于 {time.asctime(time.localtime(event_time))} 运行')
    s.run()


# 在解决方案视频中使用的参考命令
# if __name__ == '__main__':
#     schedule_function(time.time() + 1, print, 'Howdy!')
#     schedule_function(time.time() + 1, print, 'Howdy!', 'How are you?')
