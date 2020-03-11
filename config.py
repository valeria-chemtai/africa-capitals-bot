import os


class DefaultConfig(object):
    PORT = os.getenv('PORT', '55882')
    HOST = os.getenv('HOST', 'localhost')
