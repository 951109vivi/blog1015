
from flask import Flask, render_template, abort

app = Flask(__name__)

# 範例文章資料
posts = [
    {
        "id": 1,
        "title": "我的第一篇文章",
        "author": "Alice",
        "content": "大家好！這是我的第一篇部落格文章。"
    },
    {
        "id": 2,
        "title": "學習 Python Flask",
        "author": "Bob",
        "content": "Flask 是一個簡單又容易上手的 Python Web 框架。"
    },
    {
        "id": 3,
        "title": "我的程式學習心得",
        "author": "Charlie",
        "content": "每天寫一點程式，持續練習就會進步。"
    }
]


# 首頁：顯示所有文章
@app.route("/")
def index():
    return render_template("index.html", posts=posts)


# 文章內頁：依照 ID 顯示文章
@app.route("/post/<int:post_id>")
def show_post(post_id):
    post = next(
        (p for p in posts if p["id"] == post_id),
        None
    )

    if post is None:
        abort(404)

    return render_template("post.html", post=post)


if __name__ == "__main__":
    app.run(debug=True)
