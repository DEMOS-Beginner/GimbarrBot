from random import randint
from birthday import Birthday

class Helper():
	'''Class-helper for vk_api library. Make different aliases for commands'''
	def __init__(self, vk_session, api, longpoll, bot):
		'''Class initialization'''
		self.vk_session = vk_session
		self.api = api
		self.longpoll = longpoll
		self.bot = bot


		self.__init_helper_config()


	def __init_helper_config(self):
		self.modules = {'Birthday': False}


	def rand_int(self, start = 0, end = 1000000):
		'''Generate random integer with default values'''
		return randint(start, end)


	def send_chat_message(self, chat_id, message):
		'''Send message in chat'''
		self.api.messages.send(chat_id = chat_id, message = message, random_id = self.rand_int())


	def send_user_message(self, user_id, message):
		'''Send message for user'''
		self.api.messages.send(user_id = user_id, message = message, random_id = self.rand_int())


	def event_from_chat(self, event):
		'''Returns true if event from needed chat'''
		if event.from_chat and event.chat_id == self.bot.chats[self.bot.active_chat]:
			return True
		return False


	def check_modules(self):
		'''Check activated modules'''
		if self.modules['Birthday']:
			self.enable_birthday()
			self.check_birthday()


	def enable_birthday(self):
		'''Enable birthday module if not active'''
		if not hasattr(self, 'birthday'):
			self.birthday = Birthday(self.vk_session, self.api, self.longpoll)


	def check_birthday(self):
		'''Congratulate person with birthday'''
		if self.birthday.status != 1:
			self.birthday.start_messaging(self)
			self.bot.stop()