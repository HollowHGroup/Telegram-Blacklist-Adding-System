import re
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

databaseGroupID = -1001657005370
userDatabase = "usersDB.txt"
blacklistDatabase = "blacklistDB.txt"
Token = "YOUR_TOKEN_HERE"

def start(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text="🇺🇸 Hi, If you don't want to receive messages from the  @RRMessage, send me your Rival Regions profile link :)\nExample Link:\nhttps://m.rivalregions.com/#slide/profile/0123456789\n\n🇹🇷 Merhaba @RRMessage sistemi tarafından mesaj almak istemiyorsan bana Rival Regions profil linkini gönder :)\nÖrnek Link:\nhttps://m.rivalregions.com/#slide/profile/0123456789")

def save_number(update, context):
    user_id = update.effective_chat.id
    # We check if a number has been saved before.
    with open(userDatabase, "r") as file:
        if str(user_id) in file.read():
            context.bot.send_message(chat_id=user_id, text="🇺🇸 According to my database, it seems like you have already registered a profile :)\n\n🇹🇷 Veritabanıma göre daha önceden bir profil kaydedilmiş görünüyor :)")
            return

    # We use a regular expression to extract the number in the message.
    regex = r"\d+"
    match = re.search(regex, update.message.text)
    if match:
        number = match.group()
        # We are looking for the number in the file blacklistDB.txt.
        with open(blacklistDatabase, "r") as file:
            if number in file.read():
                context.bot.send_message(chat_id=user_id, text="🇺🇸 This profile has already been registered by someone else :)\n\n🇹🇷 Bu profil daha önce başkası tarafından kaydedilmiş görünüyor :)")
                return
        # We save the number in the file.
        with open(blacklistDatabase, "a") as file:
            file.write(number + "\n")
        # We save the user's ID in the userDB.txt file.
        with open(userDatabase, "a") as file:
            file.write(str(user_id) + "\n")
        # We send the message with the number to the group.
        context.bot.forward_message(chat_id=databaseGroupID, from_chat_id=update.effective_chat.id, message_id=update.message.message_id)
        context.bot.send_message(chat_id=user_id, text="🇺🇸 Profile added to the database.\n\n🇹🇷 Profil veritabanına eklendi.")
    else:
        context.bot.send_message(chat_id=user_id, text="🇺🇸 Invalid link, please send a Rival Regions profile link.\n\n🇹🇷 Geçersiz link, lütfen Rival Regions profil linkini gönderiniz.")


def main():
    # We create a Telegram bot.
    updater = Updater(token=Token, use_context=True)

    # We add commands.
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.private & Filters.text & ~Filters.command, save_number))

    # We run the bot.
    updater.start_polling()
    updater.idle()

main()