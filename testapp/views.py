from flask import render_template, request
from testapp import app
from dotenv import load_dotenv
import os  # 環境変数にアクセスするためのライブラリ。
import openai


load_dotenv()  # .envファイルに保存されている環境変数 (APIキー) を読み込み

openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":  # request.methodでリクエストの種類を確認
        # フォームから送信されたuser_message (ユーザーが入力したメッセージ) を取得
        user_message = request.form["user_message"]

        # ChatGPT APIにリクエストを送信
        response = openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                # ChatGPTの動作を指示
                {"role": "system", "content": "あなたは親切で役に立つアシスタントです。"},
                # ユーザーのメッセージをChatGPTに送信
                {"role": "user", "content": user_message},
            ],
        )
        # APIからのレスポンスからChatGPTの応答テキストを抽出
        # 改行を<br>に置換
        bot_reply = response.choices[0].message.content
        print(bot_reply)
        # print(type(bot_reply))

        # render_template()でindex.htmlをレンダリングしたうえでユーザーの入力とChatGPTの応答をHTMLに渡す
        return render_template("testapp/index.html",
                               user_message=user_message,
                               bot_reply=bot_reply
                               )

    # GETリクエストの場合のレンダリング
    return render_template("testapp/index.html")
