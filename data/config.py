from environs import Env

# Теперь используем вместо библиотеки python-dotenv библиотеку environs
env = Env()
env.read_env()

# Telegram Bot
BOT_TOKEN = env.str("BOT_TOKEN")  # Забираем значение типа str
ADMINS = env.list("ADMINS")  # Тут у нас будет список из админов


# Mailjet Api (Send mail)
API_KEY = env.str("API_KEY")
API_SECRET = env.str("API_SECRET")

# Email sender
SENDER_GMAIL = env.str("SENDER_GMAIL")
SENDER_NAME = env.str("SENDER_NAME")

# Email recipient
RECIPIENT_GMAIL = env.str("RECIPIENT_GMAIL")
RECIPIENT_NAME = env.str("RECIPIENT_NAME")


# Yookassa
SHOP_ID = env.str("SHOP_ID")
SHOP_API_TOKEN = env.str("SHOP_API_TOKEN")