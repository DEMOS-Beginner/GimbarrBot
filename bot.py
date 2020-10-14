import time
import re

from helper import Helper
from vk_api.bot_longpoll import VkBotEventType
from datetime import datetime

class Bot():
	def __init__(self, vk_session, api, longpoll, settings):
		'''Class constructor'''
		self.vk_session = vk_session
		self.api = api
		self.longpoll = longpoll

		self.timeout = settings['timeout']
		self.chats = settings['chats']
		self.active_chat = settings['active_chat']
		helper_modules = settings['helper_modules']

		self.life = True

		self.info = {
			'life': self.life,
			'last_event_time': None,
			'last_event_type': None,
		}

		self.helper = Helper(vk_session, api, longpoll, self, helper_modules)

		self.__init_triggers()


	def __init_triggers(self):

		#Triggers if self.life = True
		self.trigger_answers = {
			r'помоги|помощь|хелп|help': 'Вот, что Я умею:\n-Напишите моё имя и я приду. ',
			r'жива|жизнь|нормально|как': 'Света Ботова жива! ',
			r'спать|сон|смерть|спи': 'Света Ботова пошла спать ',
		}

		self.trigger_commands = {
			r'спать|сон|смерть|спи': 'self.stop()',
		}

		#Triggers if self.life = False
		self.sleep_answers = {
			r'встань|проснись|вставай|просыпайся|': 'Света Ботова проснулась',
		}

		self.sleep_commands = {
			r'встань|проснись|вставай|просыпайся|': 'self.up()',
		}


	def start(self):
		'''Start bot life'''
		self.say_hello()
		while True:
			time.sleep(self.timeout)
			self.helper.check_modules()	
			for event in self.longpoll.check():
				if self.life:
					self.__update_info(event)
					self.__check_messages(event)
				else:
					self.__check_triggers(event, self.sleep_answers, self.sleep_commands)


	def up(self):
		'''Up bot from sleep mode'''
		self.say_hello()
		self.life = True
		self.__update_info()


	def say_hello(self):
		'''Send message about starting'''
		message = '''
			===========================
			Света Ботова готова к работе
			___________________________
			КАК Я РАБОТАЮ:
			___________________________
			Для выполнения команды напишите моё имя и триггер
			___________________________
			Триггеры для вызова помощи: help, хелп, помощь, помоги
			===========================
		'''
		self.helper.send_chat_message(self.chats[self.active_chat], message)


	def stop(self):
		'''Kill bot proccess'''
		self.life = False
		self.__update_info()	


	def __check_messages(self, event):
		'''Checks messages event and sending messages'''
		if event.type == VkBotEventType.MESSAGE_NEW:
			if self.__event_from_chat(event):
				self.__check_message_events(event)
			if event.from_user:
				self.helper.send_user_message(event.object.message['peer_id'], 'Света Ботова жива!')


	def __check_message_events(self, event):
		'''Check differents message events'''
		if 'action' in event.object.message:
			if event.object.message['action']['type'] == 'chat_invite_user':
				self.helper.send_chat_message(event.chat_id, 'Света Ботова приветствует вас, многоуважаемый господин')
			elif event.object.message['action']['type'] == 'chat_kick_user':
				self.helper.send_chat_message(event.chat_id, 'Проваливай! Нам такие не нужны!')

		self.__check_triggers(event, self.trigger_answers, self.trigger_commands)


	def __check_triggers(self, event, triggers, commands):
		'''Check if message text like a trigger or command'''
		if self.__event_for_me(event):
			for trigger, answer in triggers.items():
				if self.__search_in_event_message(trigger, event):
					self.helper.send_chat_message(event.chat_id, answer)
					if trigger in commands:
						eval(commands[trigger])


	def __event_from_chat(self, event):
		'''Returns true if event from needed chat'''
		if event.from_chat and event.chat_id == self.chats[self.active_chat]:
			return True
		return False


	def __search_in_event_message(self, trigger, event):
		'''Search pattern match in event message'''
		message = event.object.message['text'].lower()
		return re.search(trigger, message)


	def __event_for_me(self, event):
		'''Return true if message for bot'''
		return self.__search_in_event_message(r'^света|светка|светочк|свет|светлана$', event)


	def __update_info(self, event = []):
		'''Updates log information'''
		self.info = {
			'life': self.life,
			'last_event_time': datetime.today().strftime('%Y-%m-%d %H:%M:%S'),
			'last_event_type': None,
		}
		
		if event != []:
			self.info['last_event_type'] = event.type



