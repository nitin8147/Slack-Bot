from slackclient import SlackClient


class SlackOperations:
    def __init__(self, slack_api_token: str, slack_client_id: str, slack_client_secret: str, slack_signing_secret: str, date_format: str, expiration_delta: int):
        self.slack_api_token = slack_api_token
        self.slack_client_secret = slack_client_secret
        self.slack_signing_secret = slack_signing_secret
        self.date_format = date_format
        self.expiration_delta = expiration_delta

        self.slack_client = SlackClient(slack_api_token, client_id=slack_client_id, client_secret=slack_client_secret)
