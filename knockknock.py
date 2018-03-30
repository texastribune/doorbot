import os
import json
import requests


webhook_url = os.environ.get('SLACK_WEBHOOK_URL')
payload = {'text': 'Someone is at the door!'}


def post_to_slack():
    try:
        requests.post(
            webhook_url,
            data=json.dumps(payload),
            headers={'Content-Type': 'application/json'}
        )
    except Exception as e:
        print(e.message)
