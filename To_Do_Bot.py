from telegram.ext import Updater, CommandHandler, \
    MessageHandler, Filters

from telegram import ChatAction

task = []

def insert(st):
    task.append(st)

def remove(name):
    if name not in task:
        print("Not found")
    else:
        task.remove(name)

def save():
    inpt=open("task_list.txt", "w")
    for x in task:
        inpt.write(x+"\n")
    inpt.close()

def start(bot,update):
    update.message.reply_text("Hello!")
    print("Hello!")

def nomsg(bot, update):
    bot.sendChatAction(update.message.chat_id, ChatAction.TYPING)
    update.message.reply_text("I'm sorry, I can't do that.")

def show(bot, update):
    bot.sendChatAction(update.message.chat_id, ChatAction.TYPING)
    if task == "":
        update.message.reply_text("Nothing to show.")
    else:
        for x in task:
            update.message.reply_text(x)

def rmv(bot, update, args):
    bot.sendChatAction(update.message.chat_id, ChatAction.TYPING)
    string = " ".join(str(x) for x in args)

    if string not in task:
        update.message.reply_text(string + "not found!")
    else:
        task.remove(string)
        save()
        update.message.reply_text(string + "removed successfully!")

def rmvall(bot, update, args):
    name = str(args[0])
    removed = []

    for x in task:
        if name in x:
            removed.append(x)
            task.remove(x)

    if not removed :
        update.message.reply_text("No matches.")
    else:
        save()
        name = " and ".join(str("\""+x+"\"") for x in removed)
        update.message.reply_text("The elements " + name + " successfully removed!")




def new(bot, update, args):
    bot.sendChatAction(update.message.chat_id, ChatAction.TYPING)
    string = " ".join(str(x) for x in args)
    insert(string)
    save()
    update.message.reply_text("Successfully added!")

def help(boy,update):
    update.message.reply_text("To-do Manager:\n1. Insert new task\
    \n2. Remove task\n3. Show all tasks")

inpt = open("task_list.txt")

for line in inpt:
    insert(line.strip())
inpt.close()


def main():
    """
    My First Bot
    """
    inpt=open("TOKEN.txt","r")
    updater=Updater(inpt.readline())

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start",start))
    dp.add_handler(MessageHandler(Filters.text,nomsg))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("showTasks",show))
    dp.add_handler(CommandHandler("newTask",new, pass_args=True))
    dp.add_handler(CommandHandler("removeTask",rmv,pass_args=True))
    dp.add_handler(CommandHandler("removeAllTasks",rmvall, pass_args=True))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()