from os import execle, environ
from sys import executable
from time import sleep

from Main import Config
from Main.core.decorators import app
from Main.core.types import Client, Message

@app.on_command("restart", "Restarts the whole app.", "restart")
async def restart(client: Client, message: Message):
    await message.edit("Restarting...")

    if (chat_id := Config.LOG_CHAT_ID):
        await client.send_message(chat_id, f"Restart requested by client {client.index}\n\n{message.id}:{message.chat.id}")
    
    else:
        sleep(2.5)
        await message.delete()

    args: list[str] = [executable, "-m", "Main"]
    execle(executable, *args, environ)