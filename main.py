from config import Config
from bot import Bot

#Get settings
properties = ['token', 'timeout', 'chats', 'active_chat', 'helper_modules']
config = Config(properties)

#Need for bot
settings = config.get_settings()
vk_data = config.get_vk_data()

#Extracting vk_data
vk_session = vk_data['vk_session']
api = vk_data['api']
longpoll = vk_data['longpoll']

#Start bot working
bot = Bot(vk_session, api, longpoll, settings)
bot.start()