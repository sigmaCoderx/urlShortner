#from keep_on import never_down
import json
import requests
import pyshorteners
import pyLense
from pyLense.Lense import Neurals
from pymongo import MongoClient
from telebot import telebot, TeleBot, types, custom_filters
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot.util import user_link

#never_down()
#admin_id = 5249435830
admin_id = [1944279581, 2069970688, 1365625365, 1433116770, 5249435830]

connection = "mongodb+srv://BotSettings:19932021Abc@anonyboy.jievtvp.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(connection)
db = client.Neurals
entity = db.BotSettings
admin = db.admins
#print(db.list_collection_names())
total_user = entity.count_documents({})

buttons = InlineKeyboardMarkup()
group = InlineKeyboardButton(text="⚡️Group⚡️", url="t.me/Neuralg")
channel = InlineKeyboardButton(text="⚡️Channel⚡️", url="t.me/Neuralp")
bug = InlineKeyboardButton("Report Issue", url="t.me/Neuralg")
buttons.add(group, channel, bug)

no_token = pyshorteners.Shortener()

bot = telebot.TeleBot("6609866055:AAF9iximtQlhpgG9RUo7G4SoQrdPQorcvgw",
                      parse_mode="HTML",
                      disable_web_page_preview=True)


@bot.message_handler(commands=["start"])
def start(msg):
  id = msg.from_user
  check_channel = "@Neuralp"
  not_found = False
  force_sub = bot.get_chat_member(check_channel, id.id)
  if force_sub.status == "left" or force_sub.status == "kicked" or not_found == True:
    bot.send_message(msg.chat.id,
                     "Please Join my update channel before accessing:",
                     reply_markup=buttons)
  else:
    userID = msg.from_user.id
    firstName = msg.from_user.first_name
    userName = f"@{msg.from_user.username}"
    data = {"userid": userID, "first_name": firstName, "user_name": userName}
    if entity.find_one({"userid": userID}) == None:
      on_db = entity.insert_one(data)
    else:
      pass
    bot.reply_to(
      msg,
      f"Hello dear:{user_link(msg.from_user)}😊 welcome: This is link shortner bot:\n<b>please send me valid url to get shortened link:</b>"
    )


@bot.message_handler(commands=["broadcast"])
def broadcast(msg):
  userID = msg.from_user.id
  firstName = msg.from_user.first_name
  userName = f"@{msg.from_user.username}"
  data = {"userid": userID, "first_name": firstName, "user_name": userName}
  #bot.set_state(msg.from_user.id,Mystate.text,msg.chat.id)
  if msg.from_user.id not in admin_id:
    bot.reply_to(msg, "This command is for admins only!")
  else:
    bot.reply_to(msg, "Send me a broadcasting message:")
    bot.register_next_step_handler(msg, send)


def send(msg):
  for ids in entity.find({}):
    id = ids["userid"]
    #uid = 5249435830 --admin id---
    #bot.reply_to(msg,f"""Your msg: {msg.text}\n broadcasted successfully!""")
    try:
      bot.send_message(id, f"{msg.text}", reply_markup=buttons)
    except:
      pass
  bot.reply_to(msg,f"""Your msg: {msg.text}\n broadcasted successfully!""")


@bot.message_handler(commands=["notify"])
def notify(msg):
  #send msg to specific user
  text = msg.text
  if msg.chat.id in admin_id:
    bot.reply_to(
      msg,
      "Send me with this format: <b>/id</b>\n <b>your text here in new line</b>"
    )
    bot.register_next_step_handler(msg, sendto_user)
  else:
    bot.send_message(msg.chat.id, "You are not in admins list:)")


def sendto_user(message):
  id = message.text.split("/")[1]
  msg = message.text.splitlines()
  print(msg)
  bot.send_message(id, msg[1])
  bot.reply_to(message, f"Your msg {msg[1]} delivered successfully:)")


@bot.message_handler(commands=["adminreg"])
def adminRegister(msg):
  #check user if he is allowed or not
  if msg.from_user.id in admin_id:
    #t = """Send me your information separated with(<b>|</b>) example <b>yourID|</b><b>name|</b><b>username:\n example: 5342<b>|</b>The Ep<b>|</b>@The_ep"""
    text = "Please send admin id and permission bool:True or False\n example: <b>453</b>|<b>True</b>\t acceptable with format only."
    bot.send_message(msg.chat.id, text)
    bot.register_next_step_handler(msg, getInfo)
  else:
    bot.send_message(msg.chat.id,
                     "You are not in allowed to use this command!")


def getInfo(msg):
  info = msg.text.split("|")
  adm_id = info[0]
  is_admin = info[1]
  #adm_fName = info[1]
  #adm_userName = f"@{info[2]}"
  #admin_data = {"adminID":int(adm_id),"adminName":adm_fName,"adminUsername":adm_userName}
  admin_data = {"adminID": [adm_id], "admin": is_admin}
  if admin.find_one({"adminID": adm_id}) == None:
    to_db = admin.insert_one(admin_data)
    #print(admin_data["adminUsername"])
  else:
    pass
  bot.reply_to(msg, f"Your msg: <b>{admin_data}</b> successfully saved on db!")


@bot.message_handler(commands=["totaluser"])
def count_users(msg):
  count = len(list(entity.find()))
  bot.send_message(msg.chat.id, f"We have:<b>{count} users</b> in our bot!")


@bot.message_handler(func=lambda m: True)
def get_url(msg):
  url = msg.text
  ep = Neurals(url)
  if ep.check() == "Yes":
    link = msg.text.strip()
    linkpw = f"https://api.lnk.pw/1.0/public/lnk.pw/link?long={link}"
    bit = pyshorteners.Shortener(
      api_key="38b6f0702be7bd7656ac1dab614c3598e6558344")
    #bitl = bit.bitly.short(link)
    clckru = no_token.clckru.short(link)
    isg = no_token.isgd.short(link)
    osd = no_token.osdb.short(link)
    tin = no_token.tinyurl.short(link)
    req = requests.get(linkpw)
    pw = json.loads(req.text)
    pw_r = pw["link"]
    result = f"\n{tin}\n {clckru}\n {isg}\n{osd}\n{pw_r} "
    bot.send_message(msg.chat.id,
                     result,
                     reply_to_message_id=msg.message_id,
                     reply_markup=buttons)
  else:
    bot.send_message(msg.chat.id, "Invalid url,please send valid url:)")


print("bot running.../")
bot.infinity_polling()

