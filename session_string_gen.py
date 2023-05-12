import os
from dotenv import load_dotenv

from pyrogram.client import Client

load_dotenv()

api_id: int|str = os.getenv("jj")

"""
api_id = os.getenv("API_ID") or input("Enter Your API ID: \n")
api_hash = os.getenv("API_HASH") or input("Enter Your API HASH : \n")

session_string = None

if input("Load from string session if any? y/N: ").lower() == "y":
    session_string = os.getenv("MAIN_SESSION")

with Client("", api_id, api_hash, session_string = session_string) as app: 
    app.send_message("me", f"**Your __string session__ is**: `{app.export_session_string()}`")
    print("The string session has been sent to your Saved Messaged!")

try:
    os.remove(".session")
except:
    print("No session file found as a session string was detected.")
"""