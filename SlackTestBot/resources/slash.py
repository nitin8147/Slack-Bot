from flask_restful import Resource
from SlackTestBot.operations.slack import SlackOperations
import os

slack_api_token = "jCRwq6OuQdn0mQ0iSNVCK3kf"
slack_client_id = "774098408869.762643090499"
slack_client_secret = "27850ca08d52bd855653b886c25a45ae"
slack_signing_secret = "48c541d9609183d841f21266897f5881"
date_format = os.environ.get('DATE_FORMAT', "%d-%m-%Y")
expiration_delta = int(os.environ.get('EXPIRATION_DAYS', 90))

slack_ops = SlackOperations(slack_api_token, slack_client_id, slack_client_secret, slack_signing_secret, date_format, expiration_delta)


class HelloWorld(Resource):
    def post(self):
        slack_ops.slack_client.api_call('chat.postMessage', channel="#general", text="Hello !!! Welcome to the future")


