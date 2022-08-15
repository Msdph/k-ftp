
from pyrogram import Client, filters
import time
from helper.utils import progress_for_pyrogram
import humanize
import ftplib
import os 

FTP_HOST = "130.185.79.155"
FTP_USER = "pz14205"
FTP_PASS = "12345678"

def handle(sizeWritten,totalSize):
    #global sizeWritten
   sizeWritten += 1024
   percentComplete = sizeWritten / totalSize
   print ("%s percent complete" %str(sizeWritten / totalSize))

def upftp(path,folder,filename):
    ftp = ftplib.FTP("130.185.79.155")
    ftp.login("pz14205", "12345678")
    f = open(f"{path}", "rb")
    ftp.cwd(f'/domains/pz14205.parspack.net/public_html/{folder}')
    ftp.storbinary(f"STOR {filename}", f ,1024 ,handle)
    f.close()

    """ftp = ftplib.FTP(FTP_HOST, FTP_USER, FTP_PASS)
    # force UTF-8 encoding
    ftp.encoding = "utf-8"
    #ftp.cwd('./domains/pz14205.parspack.net/public_html/')
    with open(path, "rb") as file:
        ftp.storbinary(f"STOR ./{one}/{two}", file)

    ftp.quit()"""

def checkftp(text):
    ftp = ftplib.FTP(FTP_HOST, FTP_USER, FTP_PASS)
    # force UTF-8 encoding
    ftp.encoding = "utf-8"
    ftp.cwd('./domains/pz14205.parspack.net/public_html/')
    files = []
    try:
        files = ftp.nlst()
    except ftplib.error_perm as resp:
        if str(resp) == "550 No files found":
            print ("No files in this directory")
        else:
            raise
    if text in files:
        return "exist"
    else:
        ftp.mkd(text)
        return "make"


@Client.on_message(filters.private & filters.reply)
async def replytext(client, update):
   #print(update)
   
   filess = update.reply_to_message
   text = update.text
   print(text)
   media = filess.document or filess.video or filess.audio or filess.photo
   filename = media.file_name
   file_id = media.file_id
   ms = await update.reply_text(
      text=f"در حال دانلود فایل . . .\n\nنام فایل : {filename}\nنام پوشه : {text}",
      disable_web_page_preview=True,
   )
   c_time = time.time()
   try:
      path = await client.download_media(message = filess, progress=progress_for_pyrogram,progress_args=( "𝚃𝚁𝚈𝙸𝙽𝙶 𝚃𝙾 𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳....",  ms, c_time))
      print(f"path : {path}")
   except Exception as e:
      await ms.edit(e)
      return

   await ms.edit("درحال آپلود در سایت ...")
   try :
      ftp = ftplib.FTP("130.185.79.155")
      ftp.login("pz14205", "12345678")
      checkftp(text)
      f = open(f"{path}", "rb")
      ftp.cwd(f'/domains/pz14205.parspack.net/public_html/{text}')
      ftp.storbinary(f"STOR {filename}", f )
      f.close()
      print("Success")
      await ms.edit(f"UPLOAD COPLETE \n\nhttps://s2.kenzodl.xyz/{text}/{filename}")
   except Exception as e:
      os.remove(path)
      print(f"ERROR : {e}")

