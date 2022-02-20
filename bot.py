from telegram.ext import *
import os

BOT_API = "5243536300:AAFQrJVeFQKChsh8QEbwA-pZ4k2I2gOkLAU"


def downloader(update, context):
    context.bot.get_file(update.message.document).download()
    with open("r.zip", 'wb') as f:
        context.bot.get_file(update.message.document).download(out=f)
        os.system("mkdir test")
        os.system("unzip r.zip -d test")

    root = f"{os.getcwd()}/test"

    for path, subdirs, files in os.walk(root):
        for name in files:
            with open(os.path.join(path, name), 'rb') as f:
                context.bot.sendDocument(update.message.chat_id, document=f)


#   for filename in os.listdir(f"{os.getcwd()}/test"):
#     with open(os.path.join(f"{os.getcwd()}/test", filename), 'rb') as f:
os.system("rm -rf test")

REQUEST_KWARGS = {
    'proxy_url': 'socks5://62.113.115.94:16072',
    'urllib3_proxy_kwargs': {
        'username': '',
        'password': '',
    }
}

updater = Updater(BOT_API, use_context=True, request_kwargs=REQUEST_KWARGS)

updater.dispatcher.add_handler(MessageHandler(Filters.document, downloader))

updater.start_polling()
updater.idle()
