# -*- coding:utf-8 -*-

import json
import requests

token = "xxxx"
alert_address = "https://oapi.dingtalk.com/robot/send?access_token="+token
headers = {"content-type": "application/json"}

def push_message(message):
    try:
        body_relay = {
            "jsonrpc": "2.0",
            "msgtype": "text",
            "text": {
                "content": message
            },
            "id":1
        }
        response = json.loads(requests.post(alert_address, data = json.dumps(body_relay), headers = headers).text)
        print('[send message] response: {}'.format(response))
    except Exception as e:
        print(repr(e))

message = '[test] send message test'
push_message(message)

