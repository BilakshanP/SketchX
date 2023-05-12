"""
from Main.core.helpers.http_helper import post

base = "https://batbi.me/"

async def paste(content: str):
    resp = await post(
            f"{base}api/v2/paste", data = content
        )
    
    return base + resp
"""