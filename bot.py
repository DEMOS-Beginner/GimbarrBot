import time

from helper import Helper
from vk_api.bot_longpoll import VkBotEventType

class Bot():
	def __init__(self, vk_session, api, longpoll, settings):
		'''Class constructor'''
		self.vk_session = vk_session
		self.api = api
		self.longpoll = longpoll

		self.timeout = settings['timeout']
		self.chats = settings['chats']
		self.active_chat = settings['active_chat']

		self.life = True
		self.helper = Helper(vk_session, api, longpoll, self)


	def start(self):
		'''Start bot life'''
		while self.life:
			time.sleep(self.timeout)
			self.helper.check_modules()
			for event in self.longpoll.listen():
				self.__check_messages(event)
		exit()


	def stop(self):
		'''Kill bot proccess'''
		self.life = False


	def __check_messages(self, event):
		'''Checks messages event and sending messages'''
		if event.type == VkBotEventType.MESSAGE_NEW:
			if self.helper.event_from_chat(event):
				self.helper.send_chat_message(event.chat_id, 'Света Ботова жива!')
			if event.from_user:
				self.helper.send_user_message(event.object.message['peer_id'], 'Света Ботова жива!')

