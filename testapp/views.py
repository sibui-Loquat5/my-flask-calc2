from flask import render_template, request
from testapp import app


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


@app.route("/eqform")
def eqform():
    res = render_template('testapp/eqform.html')
    return res


@app.route("/eqform/solve", methods=["POST"])
def eqform_solve():
    eq_solve = request.form["eq"]
    return f"POST受け取り内容: {eq_solve}"

# commit test
