from flask import Flask
from routes.admin import admin_bp

app = Flask(__name__)

app.register_blueprint(admin_bp)

@app.route("/")
def home():
    return {
        "status": "running",
        "service": "PW XML Generator"
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
