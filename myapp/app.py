from flask import Flask
from routes.main_routes import main_routes

app = Flask(__name__)
app.secret_key = 'your-secret-key'  # これを追加！

app.register_blueprint(main_routes, url_prefix="/")

if __name__ == "__main__":
    app.run(debug=True)





