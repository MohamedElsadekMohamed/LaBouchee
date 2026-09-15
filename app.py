"""
LaBouchee — Branch Sales Automation
تطبيق Flask بسيط بيقدّم الأداة. كل المعالجة بتحصل في المتصفح (ExcelJS مدمجة داخليًا)،
فالسيرفر بيقدّم الصفحة بس — يعني خفيف، سريع، وبيشتغل على أي استضافة مجانية.
"""
import os
from flask import Flask, send_from_directory, jsonify

app = Flask(__name__, static_folder=None)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


@app.route("/")
def index():
    # نقدّم الصفحة كملف ثابت (بدون Jinja) عشان نتجنب أي تعارض مع أكواد JS/CSS
    return send_from_directory(BASE_DIR, "index.html")


@app.route("/health")
def health():
    return jsonify(status="ok")


# كاش خفيف للأصول الثابتة
@app.after_request
def add_headers(resp):
    resp.headers["X-Content-Type-Options"] = "nosniff"
    return resp


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
