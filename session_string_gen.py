import os
from dotenv import load_dotenv

from pyrogram.client import Client

load_dotenv()

try:
    api_id: int|str = os.getenv("API_ID") or input("Enter Your API ID: \n")
    api_hash: str = os.getenv("API_HASH") or input("Enter Your API HASH : \n")

    with Client("", api_id, api_hash) as app:
        app.send_message("me", f"**Your __string session__ is**: `{app.export_session_string()}`")
        print("The string session has been sent to your Saved Messaged!")
finally:
    os.remove(".session")