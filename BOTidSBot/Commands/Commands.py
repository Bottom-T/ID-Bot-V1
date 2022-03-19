from pyrogram import filters
from pyrogram import Client as BOTidSBot
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant
from BOTidSBot.Translation import Translation
from BOTidSBot.Config import Config
from BOTidSBot.Commands.Buttons import START_BUTTON, HELP_BUTTON, ABOUT_BUTTON

UPDATE_CHANNEL=Config.UPDATE_CHANNEL # Update Channel Forces Subscribe
BOT_USERNAME=Config.BOT_USERNAME # ReStart Option 
JOIN=Translation.JOIN_TEXT # Button Text (Update Channel)
TRY=Translation.TRY_TEXT # Button Text (Update Channel)
SUB_TEXT=Translation.FSUB_TEXT # FSUB Information Text

developer="us7a5"
co_developer="us7a5"
source="https://github.com/Bottom-T/ID-Bot-V1"
mt_chat="us7a5"
mt_bot="us7a5"

@BOTidSBot.on_message(filters.private & filters.command("start"))
async def start_handler(motech, update):
    update_channel = UPDATE_CHANNEL
    if update_channel:
        try:
            user = await motech.get_chat_member(update_channel, update.chat.id)
            if user.status == "kicked out":
               await update.reply_text("🔮 𝚂𝙾𝚁𝚁𝚈 𝙳𝚄𝙳𝙴, 𝚈𝙾𝚄 𝙰𝚁𝙴 **🅤︎🅢︎🅐︎ 🇺🇸**")
               return
        except UserNotParticipant:
            #await update.reply_text(f"Join @{Channel User Name} To Use Me") From Motech.py
            await update.reply_text(
                text=f"<b>{SUB_TEXT}</b>",
                reply_markup=InlineKeyboardMarkup([
                    [ InlineKeyboardButton(text=f"{JOIN}", url=f"t.me/{UPDATE_CHANNEL}")],
                    [ InlineKeyboardButton(text=f"{TRY}", url=f"https://t.me/{BOT_USERNAME}?start=try")]
              ])
            )
            return
        except Exception:
            await update.reply_text(f"@{UPDATE_CHANNEL}")
            return  
    reply_markup =  START_BUTTON
    await update.reply_text(
        text=Translation.START_MSG.format(update.from_user.mention),
        disable_web_page_preview=True,
        reply_markup=reply_markup
  )


@BOTidSBot.on_message(filters.private & filters.command("help"))
async def help_handler(motech, update):
    update_channel = UPDATE_CHANNEL
    if update_channel:
        try:
            user = await motech.get_chat_member(update_channel, update.chat.id)
            if user.status == "kicked out":
               await update.reply_text("🔮 𝚂𝙾𝚁𝚁𝚈 𝙳𝚄𝙳𝙴, 𝚈𝙾𝚄 𝙰𝚁𝙴 **🅤︎🅢︎🅐︎ 🇺🇸**")
               return
        except UserNotParticipant:
            #await update.reply_text(f"Join @{Channel User Name} To Use Me") From Motech.py
            await update.reply_text(
                text=f"<b>{SUB_TEXT}</b>",
                reply_markup=InlineKeyboardMarkup([
                    [ InlineKeyboardButton(text=f"{JOIN}", url=f"t.me/{UPDATE_CHANNEL}")],
                    [ InlineKeyboardButton(text=f"{TRY}", url=f"https://t.me/{BOT_USERNAME}?start=try")]
              ])
            )
            return
        except Exception:
            await update.reply_text(f"@{UPDATE_CHANNEL}")
            return  
    reply_markup =  HELP_BUTTON
    await update.reply_text(
        text=Translation.HELP_MSG,
        disable_web_page_preview=True,
        reply_markup=reply_markup
  )

@BOTidSBot.on_message(filters.private & filters.command("about"))
async def about_handler(motech, update):
    update_channel = UPDATE_CHANNEL
    if update_channel:
        try:
            user = await motech.get_chat_member(update_channel, update.chat.id)
            if user.status == "kicked out":
               await update.reply_text("🔮 𝚂𝙾𝚁𝚁𝚈 𝙳𝚄𝙳𝙴, 𝚈𝙾𝚄 𝙰𝚁𝙴 **🅤︎🅢︎🅐︎ 🇺🇸**")
               return
        except UserNotParticipant:
            #await update.reply_text(f"Join @{Channel User Name} To Use Me") From Motech.py
            await update.reply_text(
                text=f"<b>{SUB_TEXT}</b>",
                reply_markup=InlineKeyboardMarkup([
                    [ InlineKeyboardButton(text=f"{JOIN}", url=f"t.me/{UPDATE_CHANNEL}")],
                    [ InlineKeyboardButton(text=f"{TRY}", url=f"https://t.me/{BOT_USERNAME}?start=try")]
              ])
            )
            return
        except Exception:
            await update.reply_text(f"@{UPDATE_CHANNEL}")
            return  
    reply_markup =  ABOUT_BUTTON
    await update.reply_text(
        text=Translation.ABOUT_MSG.format(BOT_USERNAME, developer, co_developer, mt_chat, mt_bot, source),
        disable_web_page_preview=True,
        reply_markup=reply_markup
  )
