from Main import aiohttp_session

async def paste(text: str) -> str|None:
    try:
        async with aiohttp_session as session:
            async with session.post(
                   'https://nekobin.com/api/documents', json = {
                       "content": text
                }
                ) as response:
                return f"https://nekobin.com/{(await response.json())['result']['key']}"
    
    except:
        return None