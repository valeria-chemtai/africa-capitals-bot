from botbuilder.ai.qna import QnAMaker, QnAMakerEndpoint
from botbuilder.core import ActivityHandler, MessageFactory, TurnContext
from botbuilder.schema import ChannelAccount

from flask import Config


class AfricaCapitalBot(ActivityHandler):
    def __init__(self, config: Config):
        # instantiate qnamaker
        self.qna_maker = QnAMaker(
            QnAMakerEndpoint(
                knowledge_base_id=config.QNA_KNOWLEDGEBASE_ID,
                endpoint_key=config.QNA_ENDPOINT_KEY,
                host=config.QNA_ENDPOINT_HOST,
            )
        )

    async def on_message_activity(self, turn_context: TurnContext):
        # make call to qnamaker service
        response = await self.qna_maker.get_answers(turn_context)
        if response and len(response) > 0:
            await turn_context.send_activity(MessageFactory.text(
                f'The Capital of {response[0].questions[0]} is {response[0].answer}'))
        else:
            await turn_context.send_activity(f'The Capital for the country {turn_context.activity.text} was not found.')

    async def on_members_added_activity(
        self,
        members_added: ChannelAccount,
        turn_context: TurnContext
    ):
        for member_added in members_added:
            if member_added.id != turn_context.activity.recipient.id:
                await turn_context.send_activity(
                    'Hello and welcome to African Nations Capitals bot!'
                )
