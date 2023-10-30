import requests
import os
from enum import Enum

class SlackMessage(Enum):
    BAD_POSTURE = 1
    GOOD_POSTURE = 2
    ERROR = 3


def send_message_to_slack(sm:SlackMessage):
    slack_url = os.getenv('SLACK_WEBHOOK_URL')
    if sm == SlackMessage.BAD_POSTURE:
        message = "Bad posture!"
    elif sm == SlackMessage.GOOD_POSTURE:
        message = "Good posture!"
    else:
        message = "Error!"

    # Slackにメッセージを送信するためのデータを準備
    data = {
        "text": message,
        # 他のオプションも設定できます
    }
    # Slackにメッセージを送信
    requests.post(slack_url, json = data)

if __name__ == "__main__":
    send_message_to_slack(SlackMessage.BAD_POSTURE)
    send_message_to_slack(SlackMessage.GOOD_POSTURE)
    send_message_to_slack(SlackMessage.ERROR)