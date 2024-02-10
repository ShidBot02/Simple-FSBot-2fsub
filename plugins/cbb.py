#(©)Codexbotz

from bot import Bot
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
                        text = f"<b>About this Bot:\n\n  A Telegram Bot for storing posts or files that can be accessed via a Special Link.\n\n👨‍💻 Modified by @Shidoteshika1</b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton('Aɴɪᴍᴇ Cʜᴀɴɴᴇʟ', url = 'https://t.me/Animemoviesr'),
                        InlineKeyboardButton('Oɴɢᴏɪɴɢ Aɴɪᴍᴇ', url = 'https://t.me/Infinity_Ongoing')
                    ],[
                        InlineKeyboardButton("⌬ My Owner ⌬", url = "https://t.me/Shidoteshika1")
                    ],[
                        InlineKeyboardButton("⬅️ Back", callback_data = "start"),
                        InlineKeyboardButton("⛔️ Close", callback_data = "close")
                    ]])
        )
    elif data == "help":
           await query.message.edit_text(
                        text = """<b>○ <u>BOT COMMANDS</u> ○

❏ Cᴏᴍᴍᴀɴᴅs ғᴏʀ ʙᴏᴛ Aᴅᴍɪɴs

‣ /start :</b> start the bot or get posts
<b>‣ /batch :</b> create group messages
<b>‣ /genlink :</b> create link for one post
<b>‣ /users :</b> view bot statistics
<b>‣ /broadcast :</b> broadcast Message
<b>‣ /stats :</b> checking your bot uptime

<b>➪ For more Help Contact- @ChatBox480</b>""",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🤖 About", callback_data = "about"),
                        InlineKeyboardButton("⬅️ Back", callback_data = "start")
                    ],[
                        InlineKeyboardButton("⛔️ Close ⛔️", callback_data = "close")
                ]])
        )
    elif data == "start":
        await query.message.edit_text(
                    text = """<b>Hᴇʟʟᴏ !!\n\nI ᴀᴍ Oɴʟʏ Sᴛᴏʀᴇ ғɪʟᴇs ғᴏʀ <a href='https://t.me/Animemoviesr'>infinity void ∞</a></b>""",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('⛩️ OUR OTHER CHANNELS ⛩️', url='https://t.me/animemoviesr/3171')
                ], [
                     InlineKeyboardButton("🤖 About Me", callback_data = "about"),
                     InlineKeyboardButton("❕Help", callback_data = "help")
                ],[
                     InlineKeyboardButton("⛔️ Close ⛔️", callback_data = "close")
            ]])
        )
    elif data == "command":
           await query.message.edit_text(
                        text = """<b>○ <u>BOT COMMANDS</u> ○

❏ Cᴏᴍᴍᴀɴᴅs ғᴏʀ ʙᴏᴛ Aᴅᴍɪɴs

‣ /start :</b> start the bot or get posts
<b>‣ /batch :</b> create group messages
<b>‣ /genlink :</b> create link for one post
<b>‣ /users :</b> view bot statistics
<b>‣ /broadcast :</b> broadcast Message
<b>‣ /stats :</b> checking your bot uptime

<b>➪ For more Help Contact- @ChatBox480</b>""",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("⬅️ Back", callback_data = "hstart"),
                        InlineKeyboardButton("⛔️ Close", callback_data = "close")
                    ]])
        )
    elif data == "hstart":
           await query.message.edit_text(
                        text = """<b>Hello User,

I am a simple file renamer bot that can only store files for a specific channel. You need to join below channels to use me properly.

1. Anime Channel: <a href= 'https://t.me/Animemoviesr'>infinity void ∞</a>
2. Ongoing Channel: <a href= 'https://t.me/Infinity_Ongoing'>∞ ongoing</a></b>

<b>/help</b> - Only this command you can use without joining any channel.

<b>For Contact Admins, Click Below:</b>""",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("⬅️ Back", callback_data = "hcommd"),
                        InlineKeyboardButton("⛔️ Close", callback_data = "close")
                    ]])
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
                 
