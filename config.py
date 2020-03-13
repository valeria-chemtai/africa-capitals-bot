import os


class DefaultConfig(object):
    PORT = os.getenv('PORT', '5000')
    HOST = os.getenv('HOST', 'localhost')
