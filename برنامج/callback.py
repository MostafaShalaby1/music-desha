# Copyright (C) 2021 By VeezMusicProject

from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from config import (
    ASSISTANT_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""โจ **Welcome [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**\n
๐ญ **[{BOT_NAME}](https://t.me/{BOT_USERNAME}) allows you to play music and video on groups through the new Telegram's video chats!**

๐ก **Find out all the Bot's commands and how they work by clicking on the ยป ๐ Commands button!**

๐ **To know how to use this bot, please click on the ยป โ ุฒุฑ ุงูุฏููู ุงูุฃุณุงุณู!**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        " ๐ฏ๏ธ ุฃุถููู ุฅูู ูุฌููุนุชู",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [InlineKeyboardButton("โ ุฏููู ุฃุณุงุณู", callback_data="cbhowtouse")],
                [
                    InlineKeyboardButton("๐ ุงูุงูุงูุฑ", callback_data="cbcmds"),
                    InlineKeyboardButton("โค ุงููุทูุฑ", url=f"https://t.me/{OWNER_NAME}"),
                ],
                [
                    InlineKeyboardButton(
                        "๐ฅ Official Group", url=f"https://t.me/{music_Desha}"
                    ),
                    InlineKeyboardButton(
                        "๐ฃ Official Channel", url=f"https://t.me/{music_Desha1}"
                    ),
                ],
              
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_callback_query(filters.regex("cbhowtouse"))
async def cbguides(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""โ **ุงูุฏููู ุงูุฃุณุงุณู ูุงุณุชุฎุฏุงู ูุฐุง ุงูุฑูุจูุชู:**

1.) **First, add me to your group.**
2.) **Then, promote me as administrator and give all permissions except Anonymous Admin.**
3.) **After promoting me, type /reload in group to refresh the admin data.**
3.) **Add @{ASSISTANT_NAME} to your group or type /userbotjoin to invite her.**
4.) **Turn on the video chat first before start to play video/music.**
5.) **Sometimes, reloading the bot by using /reload command can help you to fix some problem.**

๐ **If the userbot not joined to video chat, make sure if the video chat already turned on, or type /userbotleave then type /userbotjoin again.**

๐ก **If you have a follow-up questions about this bot, you can tell it on my support chat here: @{GROUP_SUPPORT}**

โก __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("๐ Go Back", callback_data="cbstart")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbcmds"))
async def cbcmds(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""โจ **Hello [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**

ยป **press the button below to read the explanation and see the list of available commands !**

โก __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("๐ท๐ป Admin Cmd", callback_data="cbadmin"),
                    InlineKeyboardButton("๐ง๐ป Sudo Cmd", callback_data="cbsudo"),
                ],[
                    InlineKeyboardButton("๐ Basic Cmd", callback_data="cbbasic")
                ],[
                    InlineKeyboardButton("๐ Go Back", callback_data="cbstart")
                ],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbbasic"))
async def cbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""๐ฎ ๐๏ธุงูุงูุงูุฑ ุงูุงุณุงุณูู:

ยป /play (song name/link) - ุจุญุซ ุนู ุงุบููู
- ุชุดุบูู ุงูุฃุบููุฉ ูุจุงุดุฑุฉ ูู ุงูููุชููุจ 
ยป /stream (query/link) - ุฅุธูุงุฑ ุฃุบููุฉ ุงููุงุฆูุฉ ูู ูุงุฆูุฉ ุงูุงูุชุธุงุฑ
ยป /vplay (video name/link) - ุชุดุบูู ุงูููุฏูู ุนูู ุฏุฑุฏุดุฉ ุงูููุฏูู
ยป /vstream - ุฑุงุจุท ูุจุงุดุฑ
ยป/ ูุงุฆูุฉ ุงูุชุดุบูู - ุชุธูุฑ ูู ูุงุฆูุฉ ุงูุชุดุบูู
ยป /playlist - ุชุธูุฑ ูู ูุงุฆูุฉ ุงูุชุดุบูู
ยป /video (query) - download video from youtube
ยป /song (query) - download song from youtube
ยป /lyric (query) - ูุต ุงูุฃุบููุฉ ุงูุบูุงุฆูุฉ
ยป /search (query) - ุงุจุญุซ ุนู ุฑุงุจุท ููุฏูู youtube

ยป /ping - show the bot ping status
ยป /uptime - show the bot uptime status
ยป /alive - show the bot alive info (in group)

โก๏ธ __Powered by {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("๐ Go Back", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbadmin"))
async def cbadmin(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""๐ฎ ๐๏ธุงูุงูุฑ ุงููุงูู:

ยป /pause - ุฅููุงู ุงูุจุซ ูุคูุชูุง (ูููุดุฑู ููุท)
ยป /resume - ุงุณุชุฆูุงู ุงูุจุซ (ุงููุดุฑู ููุท)
ยป /skip - ุงูุชุจุฏูู ุฅูู ุงูุฏูู ุงูุชุงูู
ยป /stop - ุฅููุงู ุงูุจุซ (ุงููุดุฑู ููุท)
ยป /vmute - mute the userbot on voice chat
ยป /vunmute - unmute the userbot on voice chat
ยป /reload - reload bot and refresh the admin data
ยป /userbotjoin - ุฏุนูุฉ ุงููุณุชุฎุฏู ุงูุฑูุจูุช ููุงูุถูุงู ุฅูู ุงูุฏุฑุฏุดุฉ (ุงููุดุฑู ููุท)
ยป /userbotleave - order userbot to leave from group

โก๏ธ __Powered by {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("๐ Go Back", callback_data="cbcmds")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbsudo"))
async def cbsudo(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""๐ฎ ๐๏ธุงูุงูุฑ ุงููุทูุฑูู:

ยป /rmw - clean all raw files
ยป /rmd - clean all downloaded files
ยป /leaveall - order userbot to leave from all group

โก __Powered by {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("๐ Go Back", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cls"))
async def close(_, query: CallbackQuery):
    await query.message.delete()
