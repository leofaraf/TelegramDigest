# https://my.telegram.org/apps
API_ID = "24933004"  # api id of telegram account
API_HASH = "0bac01ab44286f9ba2a19759a484d9b3"  # api hash of telegram account
PHONE_NUMBER = "79969434611"  # number of telegram account
DIGEST_CHANNEL = "digestbychatgpt"  # username of digest channel which will use to send message

# IMPORTANT: you can use ChatGPT api only which VPN if you're live in Russia
OPENAI_API_KEY = "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"  # API key for ChatGPT
OPENAI_SYSTEM_ROLE = ("Ты русскоязычный ассистент саммаризатор, " +
                      "в ответ нужно ввести summary без доп. символов, " +
                      "сообщение должно быть до 200 символов")  # plan of work chat_gpt

MAX_CHANNEL_BUFFER_LIMIT = 4000  # max amount of symbols which will have written in AI model
# if chatgpt summary give summary long than this value will have sliced, disable fn value - write 0
MAX_SUMMARY_LENGTH = 300
SUMMARY_FORMAT = """**{}**
{}"""  # first arg - channel name, second arg - text output (usually correctly summary)
DIGEST_FORMAT = """Всем привет. Дайджест по недавным постам!

{}"""  # in {} will be list of summary (SUMMARY_FORMAT), between every summary will be empty line
SCHEDULE_AT = "22:10"  # like "19:00", "21:20", "22:30"
EXCEL_FILE_NAME = "channels.xlsx"  # this file will be using as mini-db for getting channels list
