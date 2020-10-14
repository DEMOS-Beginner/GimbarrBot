import vk_api

from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from module_loader import ModuleLoader

class Config():
	'''Bot configuration'''
	def __init__(self, properties):
		'''Constructor of class'''

		#Main configuration
		self.__token = ''
		self.__timeout = 1
		self.__chats = {'Main': 1, 'Test': 2}
		self.__active_chat = 'Test'

		self.__initialize_vk()

		#Modules configurations
		self.__helper_modules = {'Birthday': False, 'Logger': True}
		self.__modules_path = 'modules'

		self.__modules_configs = {
			'Logger': {
				'args': ['log_fields'],
				'log_fields': {
					'life': True,
					'last_event_time': None,
					'last_event_type': None,
				}
			},
			'Birthday': {
				'args': ['vk_session', 'api', 'longpoll'],
				'vk_session': self._vk_session,
				'api': self._api,
				'longpoll': self._longpoll,
			}
		}

		self.properties = properties


	def __initialize_vk(self):
		'''Initialize vk_session, api, longpoll'''
		self._vk_session = vk_api.VkApi(token = self.get_token())
		self._api = self._vk_session.get_api()
		self._longpoll = VkBotLongPoll(self._vk_session, 182872536)
		self.__vk_data = ['vk_session', 'api', 'longpoll'];


	def __execute(self, function, *args):
		'''Execute function with name = function'''
		if (args != ()):
			return eval(function)(args)
		else:
			return eval(function)()


	def __get_value(self, variable):
		'''Returns value of variable'''
		return eval(variable)


	def get_settings(self):
		'''Return all require properties'''
		result = {}
		for prop in self.properties:
			function = 'self.get_' + prop
			if hasattr(self, 'get_' + prop):
				result[prop] = self.__execute(function)
			else:
				print('Не удалось получить свойство: ' + prop)

		return result


	def get_vk_data(self):
		'''Return all vk_data'''
		result = {}
		for name in self.__vk_data:
			data = 'self._' + name
			if hasattr(self, '_' + name):
				result[name] = self.__get_value(data)
			else:
				print('Не удалось получить свойство: ' + name)

		return result


	def get_token(self):
		'''Return group token'''
		return self.__token


	def get_timeout(self):
		'''Return timeout - time of pause between api queries'''
		return self.__timeout


	def get_chats(self):
		'''Return dict with chats ids'''
		return self.__chats


	def get_active_chat(self):
		'''Return active chat'''
		return self.__active_chat


	def get_helper_modules(self):
		'''Returns helper modules'''
		module_loader = ModuleLoader(self.__modules_path, self.__helper_modules, self.__modules_configs)
		modules = module_loader.get_modules()

		return modules

