import datetime
import time
from telethon.sync import TelegramClient
from telethon.tl.functions.account import UpdateProfileRequest

api_id = 26659294
api_hash = '5f162d51eb3aadfe2d76dba35424fe85' 
phone = '+998949290053' 
nicknames = [
    "Fayoz",
    "𝒻𝒶𝓎𝑜𝓏",
    "F",
    "𝐹𝒶𝓎𝑜𝓏",
    "𝐹𝓪𝕪𝑜𝕫✧",
    "𝒻𝗮𝔂ο𝑧",
    "𝗙𝖺𝕪𝖔𝖟",
    "𝐹𝓪𝑦𝑜𝑧",
    "𝓕𝒶𝔶𝔬𝔷",
    "𝗳𝒶𝕪𝔬𝕫",
    "𝒻𝖺𝓎𝖔𝖟",
    "𝐹𝔞𝕪𝕠𝕫",
    "𝐹𝒶𝔶𝖔𝔷",
    "𝒻𝖺𝕪𝖔𝕫",
    "𝓕𝒶𝔂𝑜𝓏",
    "𝓕𝖺𝕪𝖔𝖟",
    "𝐹𝒶𝔶𝑜𝔷",
    "𝒻𝔞𝓎𝔬𝔷",
    "𝒻",
    "𝔉",
    "<>",

]



client = TelegramClient('session_name', api_id, api_hash)


async def update_profile():
    index = 0
    while True:
        current_nickname = nicknames[index]

        await client(UpdateProfileRequest(first_name=f"{current_nickname}  {datetime.datetime.now().strftime('%H:%M') + datetime.timedelta(hours=4)} " ))
        print(f"Nickname updated to: {current_nickname}")

        index = (index + 1) % len(nicknames)

        time.sleep(60)


with client:
    client.loop.run_until_complete(update_profile())
