from config import BOT, BOT_USERNAME
from PHB.database import DB
from PHB.inline import check_user
from pyrogram import Client, filters, idle
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup 


@Client.on_message(filters.command("start"))
async def start_msg(client, m: Message):
    check_user(m.from_user.id)
    START_TXT = f"Hey {m.from_user.mention}! \nThis is a PornHub Downloader Bot!!"
    await m.reply(
        START_TXT,
        reply_markup=InlineKeyboardMarkup(
            [
                    [
                        InlineKeyboardButton(
                            text="Support", url="t.me/GodEyeSupport"
                        ),
                        InlineKeyboardButton(
                            text="UpDate", url="https://t.me/GodEyeUpdate"
                        ),
                    ],
                    [InlineKeyboardButton(text="Search 🎥", switch_inline_query_current_chat=query)],
                ]
            ),
        )
    
@Client.on_message(filters.command("help"))
async def help_msg(client, m: Message):
    check_user(m.from_user.id)
    START_TXT = f"Hey {m.from_user.mention}! \nThis is a PornHub Downloader Bot!!"
    await m.reply(
        START_TXT,
        reply_markup=InlineKeyboardMarkup(
            [
                    [
                        InlineKeyboardButton(
                            text="Support", url="t.me/GodEyeSupport"
                        ),
                        InlineKeyboardButton(
                            text="UpDate", url="https://t.me/GodEyeUpdate"
                        ),
                    ],
                    [InlineKeyboardButton(text="Search 🎥", switch_inline_query_current_chat=query)],
                ]
            ),
        )
    
    
@Client.on_message(filters.command("stats"))
async def stats(client, m: Message):
    check_user(m.from_user.id)
    statmsg = f"""
**📈 Sᴛᴀᴛs Fᴏʀ** @{BOT_USERNAME} :
Tᴏᴛᴀʟ Usᴇʀs - `{len(DB['USERS'].split())}`
Vɪᴅs ɪɴ DB - `{len(DB.keys())}`
"""
    await m.reply(statmsg)
