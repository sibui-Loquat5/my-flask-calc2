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
                {
                    "role": "system",
                    "content": 
                        "数式解説のフォーマット：\n"
                        "1. 解く数式をLaTeXで表示\n"
                        "2. 使用する定理/公式を明示\n"
                        "3. 計算過程をステップバイステップで導出\n"
                        "追加の指示:\n"
                        "- 変数置換がある場合は『◯◯と置く』と宣言\n"
                        "- 各ステップの数式は独立した行に表示\n"
                        "- 自然言語の説明は最小限に抑える"
                },
                # ユーザーのメッセージをChatGPTに送信
                {"role": "user", "content": user_message},
            ],
            temperature=0.2,
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
