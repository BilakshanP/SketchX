from Main.core.helpers.http_helper import post

base = "https://batbin.me/"

async def paste(content: str) -> str:
    resp = await post(f"{base}api/v2/paste", data=content)
    if not resp["success"]: # type: ignore
        return ""

    return base + resp["message"] # type: ignore