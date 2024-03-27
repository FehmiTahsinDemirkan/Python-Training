# example of gather with a list that results in an error
import asyncio


# coroutine used for a task
async def task_coro(value):
    # report a message
    print(f'>task {value} executing')
    # sleep for a moment
    await asyncio.sleep(1)


# coroutine used for the entry point
async def main():
    # report a message
    print('main starting')
    # create many coroutines
    coros = [task_coro(i) for i in range(10)]
    # run the tasks
    await asyncio.gather(coros)
    # report a message
    print('main done')


# start the asyncio program
# asyncio.run(main())
""""**************************************************************"""

# example of gather without await results in an error

# coroutine used for a task
async def task_coro1(value):
    # report a message
    print(f'>task {value} executing')
    # sleep for a moment
    await asyncio.sleep(1)


# coroutine used for the entry point
async def main1():
    # report a message
    print('main starting')
    # create many coroutines
    coros = [task_coro1(i) for i in range(10)]
    # run the tasks
    asyncio.gather(*coros)
    # report a message
    print('main done')


# start the asyncio program
asyncio.run(main1())