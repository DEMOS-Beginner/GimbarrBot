

class Logger():
	'''This class writes different log info'''
	def __init__(self, log_fields):
		'''Class constructor'''
		self.log_data = {}
		self.log_number = 0

		for field in log_fields.keys():
			self.log_data[field] = None


	def enable_module(self, bot):
		self.bot = bot
		if self.__check_updates():
			self.__console_log_info()


	def __console_log_info(self):
		'''Write log info to console on updating info'''
		print('Log #' + str(self.log_number))
		self.log_number += 1
		for key, value in self.bot.info.items():
			print(str(key) + ': ' + str(value))
			self.__update_log_data(key, value)
		print('\n')


	def __check_updates(self):
		if self.bot.info != self.log_data:
			return True
		return False


	def __update_log_data(self, key, value):
		'''Updates value in log_data'''
		self.log_data[key] = value