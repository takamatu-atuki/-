# app.py
from flask import Flask
from routes.main_routes import main_routes  # ルートをインポート

app = Flask(__name__)
app.register_blueprint(main_routes, url_prefix="/")  # 🔴 Blueprint を登録！

if __name__ == "__main__":
    app.run(debug=True)




