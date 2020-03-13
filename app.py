from bot import AfricaCapitalBot
from config import DefaultConfig


BOT = AfricaCapitalBot()
CONFIG = DefaultConfig()

async def root(request):
    return Response(text='Welcome to African Nations Capitals bot')


app = web.Application()
app.router.add_get('/api', root)


if __name__ == '__main__':
    try:
        web.run_app(app, host=CONFIG.HOST, port=CONFIG.PORT)
    except Exception as e:
        raise e
