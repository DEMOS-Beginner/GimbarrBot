import time
from random import choice

class Birthday():
	def __init__(self, vk_session, api, longpoll):
		'''Class constructor'''
		self.vk_session = vk_session
		self.api = api
		self.longpoll = longpoll
		self.status = 0

		self.__init_birthday_config()


	def __init_birthday_config(self):
		'''Initialize birthday settings'''
		self.names = ['Name', 'Name2', 'Name3']
		self.to_whom = '@user_identificator (:x:)';
		self.chat_id = 1
		self.timeout = 1200
		self.message_list = ['Happy Birthday, :name:']


	def start_messaging(self, helper):
		'''Send messages'''
		for message in self.message_list:
			to_whom = self.to_whom.replace(':x:', choice(self.names))
			message = message.replace(':name:', to_whom)
			helper.send_chat_message(self.chat_id, message);
			time.sleep(self.timeout)
		self.status = 1