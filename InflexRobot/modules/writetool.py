import requests
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode, Update
from telegram.ext import CallbackContext
from telegram.ext.dispatcher import run_async

from InflexRobot import BOT_NAME, BOT_USERNAME, dispatcher
from InflexRobot.modules.disable import DisableAbleCommandHandler


@run_async
def handwrite(update: Update, context: CallbackContext):
    message = update.effective_message
    if message.reply_to_message:
        text = message.reply_to_message.text
    else:
        text = update.effective_message.text.split(None, 1)[1]
    m = message.reply_text("Writing the text...")
    req = requests.get(f"https://api.sdbots.tk/write?text={text}").url
    message.reply_photo(
        photo=req,
        caption=f"""
Successfully Written Text ð

â¨ **Written By :** [{BOT_NAME}](https://t.me/{BOT_USERNAME})
ð¥ **Requested by :** {update.effective_user.first_name}
â **Link :** `{req}`""",
        parse_mode=ParseMode.MARKDOWN,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("â¢ á´á´Êá´É¢Êá´á´©Ê â¢", url=req),
                ],
            ]
        ),
    )
    m.delete()


__help__ = """
 Writes the given text on white page with a pen ð

â /write <text> *:* Writes the given text.
"""

WRITE_HANDLER = DisableAbleCommandHandler("write", handwrite)

dispatcher.add_handler(WRITE_HANDLER)

__mod_name__ = "WÊÉªá´á´Tá´á´Ê"
__command_list__ = ["write"]
__handlers__ = [WRITE_HANDLER]
