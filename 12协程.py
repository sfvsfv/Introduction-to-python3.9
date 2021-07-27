"""
作者：川川
时间：2021/7/27
"""

# import asyncio
# async def main():
#     print('Hello ...')
#     await asyncio.sleep(1)
#     print('... World!')
# asyncio.run(main())


'''等待 1 秒后打印 "hello"，然后 再次 等待 2 秒后打印 "world"'''
# import asyncio
# import time
#
# async def say_after(delay, what):
#     await asyncio.sleep(delay)
#     print(what)
# async def main():
#     print(f"started at {time.strftime('%X')}")
#     await say_after(1, 'hello')
#     await say_after(2, 'world')
#     print(f"finished at {time.strftime('%X')}")
# asyncio.run(main())
'''asyncio.create_task() 函数用来并发运行作为 asyncio 任务 的多个协程。'''
# async def main():
#     task1 = asyncio.create_task(
#         say_after(1, 'hello'))
#     task2 = asyncio.create_task(
#         say_after(2, 'world'))
#     print(f"started at {time.strftime('%X')}")
#     # Wait until both tasks are completed (should take
#     # around 2 seconds.)
#     await task1
#     await task2
#
#     print(f"finished at {time.strftime('%X')}")
# asyncio.run(main())



'''Python 协程属于 可等待 对象，因此可以在其他协程中被等待'''
# import asyncio
#
# async def nested():
#     return 42
#
# async def main():
#     # Nothing happens if we just call "nested()".
#     # A coroutine object is created but not awaited,
#     # so it *won't run at all*.
#     # Let's do it differently now and await it:
#     print(await nested())  # will print "42".
#
# asyncio.run(main())

'''
协程函数: 定义形式为 async def 的函数;
协程对象: 调用 协程函数 所返回的对象。
'''
'''当一个协程通过 asyncio.create_task() 等函数被封装为一个 任务，该协程会被自动调度执行'''
# import asyncio
#
# async def nested():
#     return 42
#
# async def main():
#     # Schedule nested() to run soon concurrently
#     # with "main()".
#     task = asyncio.create_task(nested())
#
#     # "task" can now be used to cancel "nested()", or
#     # can simply be awaited to wait until it is complete:
#     await task
# asyncio.run(main())


'''运行 asyncio 程序'''
'''asyncio.run(coro, *, debug=False)¶'''
# import asyncio
# async def main():
#     await asyncio.sleep(1)
#     print('hello')
#
# asyncio.run(main())

'''创建任务'''
'''asyncio.create_task(coro, *, name=None)¶'''
# import asyncio
# async def coro():
#     return 2021
# task = asyncio.create_task(coro())#python3.7+
# This works in all Python versions but is less readable
# task = asyncio.ensure_future(coro())#before python3.7


'''休眠'''
''' asyncio.sleep(delay, result=None, *, loop=None)¶'''
'''以下协程示例运行 5 秒，每秒显示一次当前日期'''
# import asyncio
# import datetime
#
# async def display_date():
#     loop = asyncio.get_running_loop()
#     end_time = loop.time() + 5.0
#     while True:
#         print(datetime.datetime.now())
#         if (loop.time() + 1.0) >= end_time:
#             break
#         await asyncio.sleep(1)
#
# asyncio.run(display_date())



'''并发运行任务'''
''' asyncio.gather(*aws, loop=None, return_exceptions=False)¶'''
# import asyncio
#
# async def factorial(name, number):
#     f = 1
#     for i in range(2, number + 1):
#         print(f"Task {name}: Compute factorial({i})...")
#         await asyncio.sleep(1)
#         f *= i
#     print(f"Task {name}: factorial({number}) = {f}")
#
# async def main():
#     # Schedule three calls *concurrently*:
#     await asyncio.gather(
#         factorial("A", 2),
#         factorial("B", 3),
#         factorial("C", 4),
#     )
#
# asyncio.run(main())


'''屏蔽取消操作'''
'''asyncio.shield(aw, *, loop=None)保护一个 可等待对象 防止其被 取消'''
# res = await shield(something())#demo
'''如果希望完全忽略取消操作 (不推荐) 则 shield() 函数需要配合一个 try/except 代码段'''
# try:
#     res = await shield(something())
# except CancelledError:
#     res = None


'''超时'''
'''asyncio.wait_for(aw, timeout, *, loop=None)¶'''
# import asyncio
# async def eternity():
#     # Sleep for one hour
#     await asyncio.sleep(3600)
#     print('yay!')
#
# async def main():
#     # Wait for at most 1 second
#     try:
#         await asyncio.wait_for(eternity(), timeout=1.0)
#     except asyncio.TimeoutError:
#         print('timeout!')
#
# asyncio.run(main())



'''简单等待'''
'''syncio.wait(aws, *, loop=None, timeout=None, return_when=ALL_COMPLETED)'''
# 用法:
# import asyncio
# done, pending = await asyncio.wait(aws)

# async def foo():
#     return 42
#
# task = asyncio.create_task(foo())
# done, pending = await asyncio.wait({task})
#
# if task in done:
#     asyncio.run(task)
#     # Everything will work as expected now.


'''在线程中运行'''
'''asyncio.to_thread(func, /, *args, **kwargs)在不同的线程中异步地运行函数 func。'''
'''这个协程函数主要是用于执行在其他情况下会阻塞事件循环的 IO 密集型函数/方法'''
# import asyncio,time
# def blocking_io():
#     print(f"start blocking_io at {time.strftime('%X')}")
#     # Note that time.sleep() can be replaced with any blocking
#     # IO-bound operation, such as file operations.
#     time.sleep(1)
#     print(f"blocking_io complete at {time.strftime('%X')}")
#
# async def main():
#     print(f"started main at {time.strftime('%X')}")
#
#     await asyncio.gather(
#         asyncio.to_thread(blocking_io),
#         asyncio.sleep(1))
#     print(f"finished main at {time.strftime('%X')}")
# asyncio.run(main())


''':要取消一个正在运行的 Task 对象可使用 cancel() 方法。调用此方法将使该 Task 对象抛出一个 CancelledError 异常给打包的协程'''
'''以下示例演示了协程是如何侦听取消请求的'''
# import asyncio
# async def cancel_me():
#     print('cancel_me(): before sleep')
#
#     try:
#         # Wait for 1 hour
#         await asyncio.sleep(3600)
#     except asyncio.CancelledError:
#         print('cancel_me(): cancel sleep')
#         raise
#     finally:
#         print('cancel_me(): after sleep')
#
# async def main():
#     # Create a "cancel_me" Task
#     task = asyncio.create_task(cancel_me())
#
#     # Wait for 1 second
#     await asyncio.sleep(1)
#
#     task.cancel()
#     try:
#         await task
#     except asyncio.CancelledError:
#         print("main(): cancel_me is cancelled now")
#
# asyncio.run(main())


'''基于生成器的协程'''
'''@asyncio.coroutine
用来标记基于生成器的协程的装饰器。
此装饰器使得旧式的基于生成器的协程能与 async/await 代码相兼容
'''
# import asyncio
# @asyncio.coroutine
# def old_style_coroutine():
#     yield from asyncio.sleep(1)
#
# async def main():
#     await old_style_coroutine()


'''队列能被用于多个的并发任务的工作量分配：'''
import asyncio
import random
import time


async def worker(name, queue):
    while True:
        # Get a "work item" out of the queue.
        sleep_for = await queue.get()

        # Sleep for the "sleep_for" seconds.
        await asyncio.sleep(sleep_for)

        # Notify the queue that the "work item" has been processed.
        queue.task_done()

        print(f'{name} has slept for {sleep_for:.2f} seconds')


async def main():
    # Create a queue that we will use to store our "workload".
    queue = asyncio.Queue()

    # Generate random timings and put them into the queue.
    total_sleep_time = 0
    for _ in range(20):
        sleep_for = random.uniform(0.05, 1.0)
        total_sleep_time += sleep_for
        queue.put_nowait(sleep_for)

    # Create three worker tasks to process the queue concurrently.
    tasks = []
    for i in range(3):
        task = asyncio.create_task(worker(f'worker-{i}', queue))
        tasks.append(task)

    # Wait until the queue is fully processed.
    started_at = time.monotonic()
    await queue.join()
    total_slept_for = time.monotonic() - started_at

    # Cancel our worker tasks.
    for task in tasks:
        task.cancel()
    # Wait until all worker tasks are cancelled.
    await asyncio.gather(*tasks, return_exceptions=True)

    print('====')
    print(f'3 workers slept in parallel for {total_slept_for:.2f} seconds')
    print(f'total expected sleep time: {total_sleep_time:.2f} seconds')


asyncio.run(main())
