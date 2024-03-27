# import asyncio
#
# from trio._tests.test_tracing import coro1, coro2
#
# # execute multiple coroutines
# asyncio.gather(coro1(), coro2())
#
# # cannot provide a list of awaitables directly
# # asyncio.gather([coro1(), coro2()])
#
# # get a future that represents multiple awaitables
# group = asyncio.gather(coro1(), coro2())
#
#
# # get a future that represents multiple awaitables
# group = asyncio.gather(coro1(), coro2())
# # suspend and wait a while, the group may be executing..
# await asyncio.sleep(10)
#
# # run the group of awaitables
# await group
#
# # run tasks and get results on one line
# results = await asyncio.gather(coro1(), coro2())
#
# try:
# 	# run tasks and get results
# 	results = await asyncio.gather(coro1(), coro2())
# except Exception as e:
#
#     # check if a gather group of tasks is done
#     if group.done():