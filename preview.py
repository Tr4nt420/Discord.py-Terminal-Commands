import discord
from discord.ext import commands
import terminalDiscordCommands as tdc
import aioconsole

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='>', intents=intents)

async def fetch_guild(guild):
    if guild.isdigit():
        guild = await bot.fetch_guild(int(guild))
        return guild
    else:
        for i in bot.guilds:
            if i.name.lower() == guild.lower():
                return i
    return False

@tdc.terminalCommand
async def listpermissions(*args, **kwargs):
    allPerms = discord.Permissions.all()
    for i, v in enumerate(allPerms.__dir__()):
        if isinstance(allPerms.__getattribute__(v), bool):
            print(v)
    return "Command succesfully executed"


@tdc.terminalCommand
async def giverole(guild, user, roles, perms):
    if len(roles) < 1: return "No roles was given"
    guild = await fetch_guild(guild)
    if not guild: return "Invalid guild"
    if user.isdigit():
        member = await guild.fetch_member(user)
    else:
        return "Invalid member ID"
    permissoids = {}
    allPerms = discord.Permissions.all().__dir__()
    for i in allPerms:
        if i.lower() in [i.lower() for i in perms]:
            permissoids[i] = perms[i]
    perms = discord.Permissions(**permissoids)

    roles_ = []
    for rolename in roles:
        roles_.append(await guild.create_role(name=rolename, permissions= perms))
    await member.add_roles(*roles_)

    return f"""Succesfully created {','.join([i.name for i in roles_])} roles of guild {guild.name} to member {member} with the permissions of 
                {', '.join([i for i in permissoids])}"""

@tdc.terminalCommand
async def listroles(guild):
    guild = await fetch_guild(guild)
    if not guild: return "Invalid guild"
    for r in await guild.fetch_roles():
        print(r.name, " ", r.id)
    return True

@tdc.terminalCommand
async def listmembers(guild):
    guild = await fetch_guild(guild)
    if not guild: return "Invalid guild"
    async for i in guild.fetch_members():
        print(i.name, " ", i.id)
    return True
                                         
@bot.event
async def on_ready():
    print("IS READY")
    await tdc.start(bot.loop)

bot.run(')
