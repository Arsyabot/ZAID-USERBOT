from Zaid import app
from pyrogram import filters


@app.on_message(filters.command("start") & filters.private)
async def start(client, message):
   await message.reply_text("Hey Zaid Userbot Assistant here")

@app.on_message(filters.command("start") & filters.private)
async def start(_, message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/7b2a3fa167686dfaa3da8.jpg",
        caption=f"""**━━━━━━━━━━━━━━━━━━━━━━━━
💥 Hᴇʟʟᴏ, I Aᴍ ᴀʟʙʏ ᴘʏʀᴏʙᴏᴛ » Aɴ Aᴅᴠᴀɴᴄᴇᴅ
Pʀᴇᴍɪᴜᴍ Tᴇʟᴇɢʀᴀᴍ Usᴇʀ Bᴏᴛ.
┏━━━━━━━━━━━━━━━━━━━┓
┣★ Oᴡɴᴇʀ'xD› : [ᴀʟʙʏ](https://t.me/Punya_Alby)
┣★ Uᴘᴅᴀᴛᴇs ›› : [Uᴘᴅᴀᴛᴇs](https://t.me/ruangprojects)
┣★ Sᴜᴘᴘᴏʀᴛ » : [Dɪsᴄᴜs](https://t.me/ruangdiskusikami)
┗━━━━━━━━━━━━━━━━━━━┛
💞 Cʟɪᴄᴋ Oɴ Dᴇᴘʟᴏʏ Bᴜᴛᴛᴏɴ Tᴏ Mᴀᴋᴇ
Yᴏᴜʀ Oᴡɴ » Gᴇɴɪᴜs Usᴇʀ Bᴏᴛ.
━━━━━━━━━━━━━━━━━━━━━━━━**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💥 Dᴇᴘʟᴏʏ Aʟʙʏ Pʏʀᴏʙᴏᴛ ✨", url=f"https://github.com/PunyaAlby/ALBY-PYROBOT")
                ]
                
           ]
        ),
    )
