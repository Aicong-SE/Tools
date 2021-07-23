from sanic import Sanic
from sanic.response import text, redirect

app = Sanic(__name__)


@app.route("/")  # 路由，
async def test(request):
    # url = app.url_for("test_params", tag=4)  # 生成url
    # return redirect(url)  # 重定向

    return text("Hello World")


@app.route("/<tag: int>", methods=["GET"])  # tag: 携带参数 int: 参数类型
async def test_params(request, tag):
    return text("Hello World")


# @app.get("/")  # 处理GET请求的简写
# async def test(request):
#     return text("Hellp World")


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8000, debug=True)
