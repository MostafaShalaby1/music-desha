from cache.admins import admins
from driver.veez import call_py
from pyrogram import Client, filters
from driver.decorators import authorized_users_only
from driver.filters import command, other_filters
from driver.queues import QUEUE, clear_queue
from driver.utils import skip_current_song, skip_item
from config import BOT_USERNAME, GROUP_SUPPORT, IMG_3, UPDATES_CHANNEL
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message


@Client.on_message(command(["تحديث قائمة الإدارة", f"reload@{BOT_USERNAME}"]) & other_filters)
@authorized_users_only
async def update_admin(client, message):
    global admins
    new_admins = []
    new_ads = await client.get_chat_members(message.chat.id, filter="administrators")
    for u in new_ads:
        new_admins.append(u.user.id)
    admins[message.chat.id] = new_admins
    await message.reply_text(
        "✅ بوت **إعادة تحميلها بشكل صحيح !**\n✅ **قائمة المسؤول** كان **محدث !**"
    )


@Client.on_message(command(["تخطي", f"تخطي@{BOT_USERNAME}", "vskip"]) & other_filters)
@authorized_users_only
async def skip(client, m: Message):

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="✨ ɢʀᴏᴜᴘ", url=f"https://t.me/{music_Desha}"
                ),
                InlineKeyboardButton(
                    text="🌻 ᴄʜᴀɴɴᴇʟ", url=f"https://t.me/{Music_Desha1}"
                ),
            ]
        ]
    )

    chat_id = m.chat.id
    if len(m.command) < 2:
        op = await skip_current_song(chat_id)
        if op == 0:
            await m.reply("❌ لا شيء يلعب حاليا")
        elif op == 1:
            await m.reply("✅ __القوائم__ فارغة.\n\n• يغادر الدردشة الصوتية")
        else:
            await m.reply_photo(
                photo=f"{IMG_3}",
                caption=f"⏭ **تم تخطي إلى المسار التالي.**\n\n🏷 **Name:** [{op[0]}]({op[1]})\n💭 **Chat:** `{chat_id}`\n💡 **Status:** `Playing`\n🎧 **Request by:** {m.from_user.mention()}",
                reply_markup=keyboard,
            )
    else:
        skip = m.text.split(None, 1)[1]
        OP = "🗑 **تمت إزالة الأغنية من قائمة الانتظار:**"
        if chat_id in QUEUE:
            items = [int(x) for x in skip.split(" ") if x.isdigit()]
            items.sort(reverse=True)
            for x in items:
                if x == 0:
                    pass
                else:
                    hm = await skip_item(chat_id, x)
                    if hm == 0:
                        pass
                    else:
                        OP = OP + "\n" + f"**#{x}** - {hm}"
            await m.reply(OP)


@Client.on_message(
    command(["ايقاف", f"ايقاف@{BOT_USERNAME}", "انهاء", f"انهاء@{BOT_USERNAME}", "ايقاف"])
    & other_filters
)
@authorized_users_only
async def stop(client, m: Message):
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.leave_group_call(chat_id)
            clear_queue(chat_id)
            await m.reply("✅ **انتهى البث.**")
        except Exception as e:
            await m.reply(f"🚫 **خطأ:**\n\n`{e}`")
    else:
        await m.reply("❌ **لا شيء في التدفق**")


@Client.on_message(
    command(["وقف تشغيل الاغنيه الحاليه", f"وقف تشغيل الاغنيه الحاليه@{BOT_USERNAME}", "وقف تشغيل الاغنيه الحاليه"]) & other_filters
)
@authorized_users_only
async def pause(client, m: Message):
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.وقفة_تيار(chat_id)
            await m.reply(
                "⏸ **تم إيقاف المسار مؤقتًا.**\n\n• **لاستئناف الدفق, استخدم ال**\n» /استئناف القيادة."
            )
        except Exception as e:
            await m.reply(f"🚫 **خطأ:**\n\n`{e}`")
    else:
        await m.reply("❌ **لا شيء في التدفق**")


@Client.on_message(
    command(["استئناف تشغيل الأغنية", f"استئناف تشغيل الأغنية@{BOT_USERNAME}", "vresume"]) & other_filters
)
@authorized_users_only
async def resume(client, m: Message):
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.استئناف_تيار_(chat_id)
            await m.reply(
                "▶️ **استأنف المسار.**\n\n• **لإيقاف البث مؤقتًا ، استخدم ملف**\n» /أمر وقفة."
            )
        except Exception as e:
            await m.reply(f"🚫 **خطأ:**\n\n`{e}`")
    else:
        await m.reply("❌ **لا شيء في التدفق**")


@Client.on_message(
    command(["كتم الصوت", f"mute@{BOT_USERNAME}", "vmute"]) & other_filters
)
@authorized_users_only
async def mute(client, m: Message):
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.mute_stream(chat_id)
            await m.reply(
                "🔇 **تم كتم صوت البوت.**\n\n• **لإلغاء كتم صوت المستخدم الروبوت, استخدم ال**\n» /أمر كتم الصوت."
            )
        except Exception as e:
            await m.reply(f"🚫 **خطأ:**\n\n`{e}`")
    else:
        await m.reply("❌ **لا شيء في التدفق**")


@Client.on_message(
    command(["غير كتم الصوت", f"غير كتم الصوت@{BOT_USERNAME}", "vunmute"]) & other_filters
)
@authorized_users_only
async def unmute(client, m: Message):
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.إعادة الصوت(chat_id)
            await m.reply(
                "🔊 **تم إعادة صوت البوت.**\n\n• **لكتم صوت المستخدم الروبوت, use the**\n» /mute command."
            )
        except Exception as e:
            await m.reply(f"🚫 **خطأ:**\n\n`{e}`")
    else:
        await m.reply("❌ **لا شيء في التدفق**")


@Client.on_message(
    command(["volume", f"volume@{BOT_USERNAME}", "vol"]) & other_filters
)
@authorized_users_only
async def change_volume(client, m: Message):
    range = m.command[1]
    chat_id = m.chat.id
    try:
        await call_py.change_volume_call(chat_id, volume=int(range))
        await m.reply(f"✅ **ضبط الصوت على** `{نطاق}`%")
    except Exception as e:
        await m.reply(f"🚫 **خطأ:**\n\n{e}")
