class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    API_ID = "1028282"
    API_HASH = "eb06d4abfb49dc3eeb1aeb98ae0f581e"

    CASH_API_KEY = "DHJE5G4EBLF8Z7ZR"  # Get this value for currency converter from https://www.alphavantage.co/support/#api-key

    DATABASE_URL = ""  # A sql database url from elephantsql.com

    EVENT_LOGS = "-1001874242997"  # Event logs channel to note down important bot level events

    MONGO_DB_URI = ""  # Get ths value from cloud.mongodb.com

    # Telegraph link of the image which will be shown at start command.
    START_IMG = "https://te.legra.ph/file/834a34c3beb2e8240f8c7.jpg"

    SUPPORT_CHAT = "InflexSupport"  # Your Telegram support group chat username where your users will go and bother you

    TOKEN = "7299383822:joininflexupdatesandsupport"  # Get bot token from @BotFather on Telegram

    TIME_API_KEY = "HYMM0KD6U518"  # Get this value from https://timezonedb.com/api

    OWNER_ID = "5747402681"  # User id of your telegram account (Must be integer)

    # Optional fields
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS = []  # User id of sudo users
    DEV_USERS = []  # User id of dev users
    DEMONS = []  # User id of support users
    TIGERS = []  # User id of tiger users
    WOLVES = []  # User id of whitelist users

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
