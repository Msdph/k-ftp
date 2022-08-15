import os
if bool(os.environ.get("WEBHOOK", False)):
    from config import Config
else:
    from config import Config
from pyrogram import Client, filters

@Client.on_message(filters.command(["start"]) & filters.private)
async def start(bot, update):
    await update.reply_text(
        text="به ربات ارسال فایل به هاست دانلود نیم بها خوش آمدی .",
        disable_web_page_preview=True,
        #reply_markup=Script.START_BUTTONS
    )

@Client.on_message(filters.command(["help"]) & filters.private)
async def help(bot, update):
    await update.reply_text(
        text="هرفایلی که بفرستی کافیه روش ریپلی کنی و اسم پوشه اش رو بدی .",
        disable_web_page_preview=True,
        #reply_markup=Script.START_BUTTONS
    )
