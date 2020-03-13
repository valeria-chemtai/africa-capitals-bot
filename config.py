import os


class DefaultConfig(object):
    APP_ID = os.getenv('MicrosoftAppId', '')
    APP_PASSWORD = os.getenv('MicrosoftAppPassword', '')
    PORT = os.getenv('PORT', '5000')
    HOST = os.getenv('HOST', 'localhost')

    QNA_KNOWLEDGEBASE_ID = os.environ.get('QNA_KNOWLEDGEBASE_ID', '')
    QNA_ENDPOINT_KEY = os.environ.get('QNA_ENDPOINT_KEY', '')
    QNA_ENDPOINT_HOST = os.environ.get('QNA_ENDPOINT_HOST', '')
