from aiohttp import ClientSession
from typing import Callable, Coroutine, Any

from Main.core.errors.error import PasteException

async def hastebin(text: str, aiohttp_session: ClientSession) -> str:
    async with aiohttp_session as session:
        async with session.post(
            "https://hastebin.com/documents",
            data = text
        ) as response:
            json = await response.json()
            id = json["key"]
            return f"https://hastebin.com/{id}"

async def nekobin(text: str, aiohttp_session: ClientSession) -> str:
    async with aiohttp_session as session:
        async with session.post("https://nekobin.com/api/documents", json = { "content": text}) as response:
            json = await response.json()
            id = json['result']['key']
            return f"https://nekobin.com/{id}"

async def spacebin(text: str, aiohttp_session: ClientSession) -> str:
    async with aiohttp_session as session:
        async with session.post("https://spaceb.in/api/v1/documents", data = { "content": text, "extension": "txt" }) as response:
            json = await response.json()
            id = json['payload']['id']
            return f"https://spaceb.in/{id}"

# async def pastebin(text: str) -> str: ...

class Paste:
    index: list[int] = [0]
    pastes: list[Callable[[str, ClientSession], Coroutine[Any, Any, str]]] = [hastebin, nekobin, spacebin]

    aiohttp_session = ClientSession()

    @staticmethod
    def circulate_and_choose() -> tuple[int, Callable[[str, ClientSession], Coroutine[Any, Any, str]]]:
        Paste.index[0] += 1
        Paste.index[0] %= len(Paste.pastes)

        return (paste_index := Paste.index[0]), Paste.pastes[paste_index]

async def paste(text: str) -> tuple[str, str]:
    tries: int = 0
    collected_exceptions: list[Exception] = []

    while tries < len(Paste.pastes):
        _, bin = Paste.circulate_and_choose()

        try:
            result: str = await bin(text, Paste.aiohttp_session)
        except Exception as e:
            tries += 1
            collected_exceptions.append(e)
            continue

        return bin.__name__.title(), result

    formatted_exceptions = "\n\n".join([f"{type(e).__name__}: {str(e)}".replace('\n', '\n' + ' ' * 8) for e in collected_exceptions])

    raise PasteException("Couldn't paste the text.\n\n" + formatted_exceptions)
