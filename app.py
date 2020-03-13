import datetime
import traceback

from aiohttp import web
from aiohttp.web import Request, Response
from botbuilder.core import (
    BotFrameworkAdapter,
    BotFrameworkAdapterSettings,
    TurnContext,
)
from botbuilder.schema import Activity, ActivityTypes

from bot import AfricaCapitalBot
from config import DefaultConfig


BOT = AfricaCapitalBot()
CONFIG = DefaultConfig()
SETTINGS = BotFrameworkAdapterSettings(CONFIG.APP_ID, CONFIG.APP_PASSWORD)
ADAPTER = BotFrameworkAdapter(SETTINGS)


async def root(request: Request) -> Response:
    return Response(text='Welcome to African Nations Capitals bot')


async def on_error(self, context: TurnContext, error: Exception):
        """
        This catches all errors and logs them to console log
        TODO: log errors to Azure application insights once deployed.
        """
        print(f"\n [on_turn_error]: { error }", file=sys.stderr)
        traceback.print_exc()
        # Send a message to the user
        await context.send_activity("Oops. Something went wrong with African Nations Capitals bot!")

        # send trace activity to bot framework emulator
        if context.activity.channel_id == "emulator":
            # create a trace activity with error object
            trace_activity = Activity(
                label="TurnError",
                name="on_turn_error Trace",
                timestamp=datetime.datetime.utcnow(),
                type=ActivityTypes.trace,
                value=f"{error}",
                value_type="https://www.botframework.com/schemas/error",
            )
            # Send a trace activity, which will be displayed in Bot Framework Emulator
            await context.send_activity(trace_activity)

ADAPTER.on_turn_error = on_error


# Listen for incoming requests on /africa-capitals/messages
async def messages(request: Request) -> Response:
    # Bot message handler.
    pass


app = web.Application()
app.router.add_get('/api', root)
app.router.add_post('/api/messages', messages)


if __name__ == '__main__':
    try:
        web.run_app(app, host=CONFIG.HOST, port=CONFIG.PORT)
    except Exception as e:
        raise e
