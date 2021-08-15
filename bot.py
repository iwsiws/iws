from telebot import *
from telebot.types import *

admin_id = 267122534
token = "1842000097:AAFv0_lmbXh1gb9GqyNcsQubo9uEXmVKiIo"
bot = TeleBot(token)

markup = ReplyKeyboardMarkup(resize_keyboard = True, one_time_keyboard = True)
markup.add("✅ RO`YHATDAN O`TISH")

@bot.message_handler(commands = ['start'])
def start(m):
	if m.chat.id == admin_id:
		matn = "Xush kelibsiz, IWS Consulting'dan kimdir royhatdan o'tsa. Men sizga malumot beraman."
		bot.send_message(admin_id, matn)
	else:
		user = m.from_user
		matn = f'''{user.first_name} Assalomu alaykum,  "IWS Consulting" rasmiy botiga xush kelibsiz! Ma'lumotlaringizni qoldirish uchun "✅ RO`YHATDAN O`TISH" tugmasini bosing 👇'''
		bot.send_message(m.chat.id, matn, reply_markup = markup)

info = []

@bot.message_handler(content_types = ["text"])
def main(m):
	try:
		if m.text == "✅ RO`YHATDAN O`TISH":
			matn = "Ma'lumotlaringizni to'gri va aniq yozing."
			bot.send_message(m.chat.id, matn, reply_markup = ReplyKeyboardRemove(selective = True))
			text = "[1/4] Ism va familyangizni kiriting.\nMasalan: Anvar Arislonov"
			a = bot.send_message(m.chat.id, text)
			bot.register_next_step_handler(a, ism)
		else:
			bot.send_message(m.chat.id, "Iltimos, faqat aytilgan tugmani bosing.")
	except:
		bot.send_message(m.chat.id, "Xato yuz berdi, iltimos /start buyrug'ini qaytadan bosing.")
try:
	def ism(m):
		info.append(m.text)
		matn = "[2/4] Telefon raqamingizni kiriting. \nMisol uchun: +998 97 030 41 44"
		a = bot.send_message(m.chat.id, matn)
		bot.register_next_step_handler(a, raqam)
		
	def raqam(m):
		var = m.text.split('+')[1]
		if len(var.split()) == 5:
			info.append(m.text)
			matn = "[3/4] Viloyatingizni yozing:\n\nMisol uchun: Toshkent shaxar"
			a = bot.send_message(m.chat.id, matn)
			bot.register_next_step_handler(a, manzil)
		else:
			matn = "Xato, namunaga etibor bering."
			v = bot.send_message(m.chat.id, matn)
			bot.register_next_step_handler(v, ism)
		
	loc = InlineKeyboardMarkup()
	btn1 = InlineKeyboardButton("Kunduzgi talim", callback_data = "kunduz")
	btn2 = InlineKeyboardButton("Sirtqi talim", callback_data = "sirt")
	loc.add(btn1, btn2)
	
	def manzil(m):
		info.append(m.text)
		matn = "[4/4] Chet el Universitetidagi ta'lim turini tanlang:"
		a = bot.send_message(m.chat.id, matn, reply_markup = loc)
		bot.register_next_step_handler(a, end)
	
	@bot.callback_query_handler(func =  lambda call: True)
	def end(m):
		if m.data == "kunduz":
			info.append("Kunduzgi talim")
		else:
			info.append("Sirtgi talim")
		matn = f"""👏 {info[0]} Tabriklaymiz! Siz omadli ro'yhatdan o'tingiz!
	
	Siz bilan tez orada menedjerlarimiz bog‘lanishadi.
	
	©️ Hurmat bilan, "IWS Consulting" jamoasi.
	
	📲 Murojaat uchun: +998 97 030 41 44 | +998 97 030 42 44"""
		text = f"Ism va familya: {info[0]}\nTelefon raqam: {info[1]}\nManzil: {info[2]}\nTalim turi: {info[3]}"
		bot.send_message(admin_id, text)
		bot.send_message(m.message.chat.id, matn)
except:
	bot.send_message(m.chat.id, "Xato yuz berdi, iltimos /start buyrug'ini qaytadan bosing.")
bot.polling()