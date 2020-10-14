import datetime

from random import randint

class Helper():
	'''Class-helper for vk_api library. Make different aliases for commands.
	   Haves custom modules for bot.'''
	def __init__(self, vk_session, api, longpoll, bot, modules):
		'''Class initialization'''
		self.vk_session = vk_session
		self.api = api
		self.longpoll = longpoll
		self.bot = bot
		self.modules_statuses = modules['Modules']
		self.modules_objects = modules['Data']


	def rand_int(self, start = 0, end = 1000000):
		'''Generate random integer with default values'''
		return randint(start, end)


	def now(self):
		'''Returns a date'''
		today = datetime.datetime.today()
		str_result = today.strftime("%Y-%m-%d %H:%M:%S")
		return str_result


	def send_chat_message(self, chat_id, message):
		'''Send message in chat'''
		self.api.messages.send(chat_id = chat_id, message = message, random_id = self.rand_int())


	def send_user_message(self, user_id, message):
		'''Send message for user'''
		self.api.messages.send(user_id = user_id, message = message, random_id = self.rand_int())


	def check_modules(self):
		'''Check activated modules'''
		for module_name, status in self.modules_statuses.items():
			if status:
				self.modules_objects[module_name].enable_module(self.bot);


	def check_birthday(self):
		'''Congratulate person with birthday'''
		if self.birthday.status != 1:
			self.birthday.start_messaging(self)
			self.bot.stop()