# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot module for getting information about the server. """

from asyncio import create_subprocess_exec as asyncrunapp
from asyncio.subprocess import PIPE as asyncPIPE
from os import remove
from platform import python_version, uname
from shutil import which

from telethon import version

from userbot import CMD_HELP, is_mongo_alive, is_redis_alive, ALIVE_NAME, BOT_VER
from userbot.events import register

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================



@register(outgoing=True, pattern="^.db$")
async def amireallydbs(dbs):
    if not is_mongo_alive() and not is_redis_alive():
        db = "Both Mongo and Redis Database seems to be failing!"
    elif not is_mongo_alive():
        db = "Mongo DB seems to be failing!"
    elif not is_redis_alive():
        db = "Redis Cache seems to be failing!"
    else:
        db = "Databases functioning normally!"
    await dbs.edit(""
                     f"`User:` {DEFAULTUSER} \n"
                     f"`Database status: {db}\n`"
                     f"`XBOT-REMIX: {BOT_VER}`"
                     "")
                     
                     
                     

