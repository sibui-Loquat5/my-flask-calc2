from flask import render_template, request
from testapp import app
from dotenv import load_dotenv
import os  # 環境変数にアクセスするためのライブラリ。
import openai


load_dotenv()  # .envファイルに保存されている環境変数 (APIキー) を読み込み

openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route('/')
def index():
    mydict = {
        "insert_something1": "viewsのinsert_something1部分",
    }
    return render_template("testapp/index.html", mydict=mydict)


@app.route('/test')
def testhtml():
    test_dict = {
        "test_message": "test.htmlの埋め込み",
    }
    return render_template("testapp/test.html", test_dict=test_dict)


@app.route("/sampleform", methods=["GET", "POST"])
def sample_form():
    if request.method == "GET":
        return render_template('testapp/sampleform.html')

    if request.method == "POST":
        print("デバッグ用POST受け取りメッセージ")
        sample_post_req = request.form["data1"]
        return f"POST受け取り内容: {sample_post_req}"


@app.route("/eqform", methods=["GET", "POST"])
def eqform():
    if request.method == "POST":  # request.methodでリクエストの種類を確認
        # フォームから送信されたuser_message (ユーザーが入力したメッセージ) を取得
        user_message = request.form["user_message"]

        # ChatGPT APIにリクエストを送信
        response = openai.chat.completions.create(
            model="gpt-4o",
            messages=[
                # ChatGPTの動作を指示
                {"role": "system", "content": "あなたは親切で役に立つアシスタントです。"},
                # ユーザーのメッセージをChatGPTに送信
                {"role": "user", "content": user_message},
            ],
        )
        # APIからのレスポンスからChatGPTの応答テキストを抽出
        bot_reply = response.choices[0].message.content
        # print(bot_reply)

        # render_template()でindex.htmlをレンダリングしたうえでユーザーの入力とChatGPTの応答をHTMLに渡す
        return render_template("testapp/eqform.html",
                               user_message=user_message,
                               bot_reply=bot_reply
                               )

    # GETリクエストの場合のレンダリング
    return render_template("testapp/eqform.html")


# @app.route("/eqform/solve", methods=["POST"])
# def eqform_solve():
#    eq_solve = request.form["eq"]
#    return f"POST受け取り内容: {eq_solve}"
