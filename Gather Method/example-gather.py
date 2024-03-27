# example of gather for one coroutine
import asyncio


# coroutine used for a task
async def task_coro():
    # report a message
    print('task executing')
    # sleep for a moment
    await asyncio.sleep(1)


# coroutine used for the entry point
async def main():
    # report a message
    print('main starting')
    # create a coroutine
    coro = task_coro()
    # gather one coroutine
    await asyncio.gather(coro)
    # report a message
    print('main done')


# start the asyncio program
# asyncio.run(main())
""""**************************************************************"""


# example of gather for many coroutines


# coroutine used for a task
async def task_coro2(value):
    # report a message
    print(f'>task {value} executing')
    # sleep for a moment
    await asyncio.sleep(1)


# coroutine used for the entry point
async def main2():
    # report a message
    print('main starting')
    # run the tasks
    await asyncio.gather(task_coro2(0),
                         task_coro2(1),
                         task_coro2(2))
    # report a message
    print('main done')


# start the asyncio program
# asyncio.run(main2())
""""**************************************************************"""


# example of gather for many coroutines in a list

# coroutine used for a task
async def task_coro3(value):
    # report a message
    print(f'>task {value} executing')
    # sleep for a moment
    await asyncio.sleep(1)


# coroutine used for the entry point
async def main3():
    # report a message
    print('main starting')
    # create many coroutines
    coros = [task_coro3(i) for i in range(10)]
    # run the tasks
    await asyncio.gather(*coros)
    # report a message
    print('main done')


# start the asyncio program
# asyncio.run(main3())

""""**************************************************************"""


# example of gather for many coroutines that return values

# coroutine used for a task
async def task_coro4(value):
    # report a message
    print(f'>task {value} executing')
    # sleep for a moment
    await asyncio.sleep(1)
    # return a value
    return value * 10


# coroutine used for the entry point
async def main4():
    # report a message
    print('main starting')
    # create many tasks
    tasks = [task_coro4(i) for i in range(10)]
    # run the tasks
    values = await asyncio.gather(*tasks)
    # report the values
    print(values)
    # report a message
    print('main done')


# start the asyncio program
# asyncio.run(main4())

""""**************************************************************"""

# example of gather nested groups of coroutines

# coroutine used for a task
async def task_coro5(value):
    # report a message
    print(f'>task {value} executing')
    # sleep for a moment
    await asyncio.sleep(1)


# coroutine used for the entry point
async def main5():
    # report a message
    print('main starting')
    # create group level 1
    group1 = asyncio.gather(task_coro5(0), task_coro5(1), task_coro5(2))
    # create group level 2
    group2 = asyncio.gather(task_coro5(3), task_coro5(4), task_coro5(5))
    # create group level 3
    group3 = asyncio.gather(group1, group2)
    # execute 3, which executes 1 and 2
    await group3
    # report a message
    print('main done')


# start the asyncio program
# asyncio.run(main5())

""""**************************************************************"""

# example of gather with of tasks and coroutines

# coroutine used for a task
async def task_coro6(value):
    # report a message
    print(f'>task {value} executing')
    # sleep for a moment
    await asyncio.sleep(1)


# coroutine used for the entry point
async def main6():
    # report a message
    print('main starting')
    # create a mix of awaitables
    awaitables = [task_coro6(0),
                  asyncio.create_task(task_coro6(1)),
                  task_coro6(2),
                  asyncio.create_task(task_coro6(3)),
                  task_coro6(4), ]
    # schedule the group
    _ = asyncio.gather(*awaitables)
    # wait around for a while
    await asyncio.sleep(2)
    # report a message
    print('main done')


# start the asyncio program
asyncio.run(main6())