import os


class DefaultConfig(object):
    APP_ID = os.getenv("MicrosoftAppId", "")
    APP_PASSWORD = os.getenv("MicrosoftAppPassword", "")
    PORT = os.getenv('PORT', '5000')
    HOST = os.getenv('HOST', 'localhost')
