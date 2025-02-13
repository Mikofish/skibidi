import os
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.models import MessageEvent, TextMessage, TextSendMessage

app = Flask(__name__)

# 設定 LINE Bot 的 Channel Access Token 和 Channel Secret
LINE_CHANNEL_ACCESS_TOKEN = 'Your Channel Access Token'
LINE_CHANNEL_SECRET = 'Your Channel Secret'

line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)
line_handler = WebhookHandler(LINE_CHANNEL_SECRET)

# Webhook 接收訊息的路由
@app.route("/callback", methods=['POST'])
def callback():
    # 確認 X-Line-Signature 是否正確
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    
    try:
        # 處理訊息
        line_handler.handle(body, signature)
    except Exception as e:
        print(f"處理錯誤: {e}")
        abort(400)

    return 'OK'

# 設定處理訊息的邏輯
@line_handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    # 回傳用戶發送的訊息
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text='你說的是: ' + event.message.text)
    )

if __name__ == "__main__":
    app.run(debug=True)
