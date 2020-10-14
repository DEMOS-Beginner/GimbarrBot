from importlib import import_module

class ModuleLoader():
	'''This class loads modules for bot'''
	def __init__(self, modules_path, modules_list, modules_configs):
		self.__path = modules_path
		self.__list = modules_list
		self.__configs = modules_configs


	def get_modules(self):
		'''
		Imports modules. Returns dict:
		{
			'Data': {
				'ModuleName1': <object>,
				'ModuleName2': <object>
			},
			'Modules': {
				'ModuleName1': False,
				'ModuleName2': True
			}
		}
		'''
		#Init result dictionary form
		result = {'Data': {}, 'Modules': {}}

		#Importing and creating needle classes
		for module_name, status in self.__list.items():
			if status:
				#Import module
				module_path = self.__path + '.' + module_name.lower()
				module = import_module(module_path)

				#Form class_path
				class_name = module_name.capitalize()
				class_path = 'module.' + class_name

				#Getting arguments for module
				arguments = self.__get_arguments(class_name)

				#Creating class object
				class_object = eval(class_path)(*arguments)

				result['Modules'][class_name] = status
				result['Data'][class_name] = class_object

		return result


	def __get_arguments(self, class_name):
		'''Returns arguments for module'''
		args_names = self.__configs[class_name]['args']
		arguments = [];
		for arg in args_names:
			if arg in self.__configs[class_name]:
				arguments.append(self.__configs[class_name][arg])
			else:
				print('Failed to get argument value:  ' + arg)
				print('Imported class: ' + class_name)

		return arguments