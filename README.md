# Discord.py-Terminal-Commands
You can now run commands from your terminal with arguments

Requirements:

``discord.py``
``aioconsole``

Example Usage:
```python
import discord
from discord.ext import commands
import terminalDiscordCommands as tdc
import aioconsole

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='>', intents=intents)

@tdc.terminalCommand
async def listmembers(guild):
    guild = await fetch_guild(guild)
    if not guild: return "Invalid guild"
    async for i in guild.fetch_members():
        print(i.name, " ", i.id)
    return True

#No arguments command
@tdc.terminalCommand
async def listpermissions(*args, **kwargs):
    allPerms = discord.Permissions.all()
    for i, v in enumerate(allPerms.__dir__()):
        if isinstance(allPerms.__getattribute__(v), bool):
            print(v)
    return "Command succesfully executed"


@bot.event
async def on_ready():
    print("IS READY")
    await tdc.start(bot.loop)

bot.run(')
```

**For more examples see preview.py**
