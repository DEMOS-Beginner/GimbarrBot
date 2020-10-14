INSTRUCTION TO START BOT:
	1. Copy config.default.py to config.py
	2. Tune config.py
	3. Start main.py script

CONFIG.PY REVIEW:
	Main configuration:
		token - it is token of your vk group;
		timeout - it is pause for checking events (default 1 sec);
		chats - you can create anymore count of chats,
			dictionary keys - it is your key title for chat (any)
			dictionary values - it is chat_id, you can find when do `print(event)` in bot.py;
		active_chat - indicate chat key from last dictionary;

	Modules configurations:
		helper_modules - dictionary with name of module and his status,
			keys - name of module,
			values - status of module (if False, then module will not enabled);
		modules_path - where stored a modules;
		modules_configs - configs for modules
			ModuleName:
				args - list with args which needed for class constructor of module;
				other keys - it is args and values;

bot.py - main bot file.
helper.py - it is class with aliases for bot functions and it is ModuleManager
module_loader.py - it is class which loads modules (don't touch it)

