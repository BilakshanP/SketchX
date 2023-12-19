# from typing import Any
# from asyncio import gather

# from Main import aiohttp_session as session

# async def get(url: str, *args: Any, **kwargs: Any):
#     async with session.get(url, *args, **kwargs) as resp:
#         try:
#             data = await resp.json()
#         except Exception:
#             data = await resp.text()
#     return data


# async def head(url: str, *args: Any, **kwargs: Any):
#     async with session.head(url, *args, **kwargs) as resp:
#         try:
#             data = await resp.json()
#         except Exception:
#             data = await resp.text()
#     return data


# async def post(url: str, *args: Any, **kwargs: Any):
#     async with session.post(url, *args, **kwargs) as resp:
#         try:
#             data = await resp.json()
#         except Exception:
#             data = await resp.text()
#     return data


# async def multiget(url: str, times: int, *args: Any, **kwargs: Any):
#     return await gather(*[get(url, *args, **kwargs) for _ in range(times)])


# async def multihead(url: str, times: int, *args: Any, **kwargs: Any):
#     return await gather(*[head(url, *args, **kwargs) for _ in range(times)])


# async def multipost(url: str, times: int, *args: Any, **kwargs: Any):
#     return await gather(*[post(url, *args, **kwargs) for _ in range(times)])



# async def resp_get(url: str, *args: Any, **kwargs: Any):
#     return await session.get(url, *args, **kwargs)

# async def resp_post(url: str, *args: Any, **kwargs: Any):
#     return await session.post(url, *args, **kwargs)