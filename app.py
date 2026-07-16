from flask import Flask
from routes.admin import admin_bp
from pathlib import Path
import os

app = Flask(__name__)

app.register_blueprint(admin_bp)


@admin_bp.get("/debug")
def debug():

    return {
        "cwd": os.getcwd(),
        "files": os.listdir("."),
        "details_exists": Path("details.xml").exists(),
        "teacher_exists": Path("teacher_details.xml").exists(),
        "details_xlsx": Path("details.xlsx").exists(),
        "teacher_xlsx": Path("teacher_details.xlsx").exists(),
    }
@app.route("/")
def home():
    return {
        "status": "running",
        "service": "PW XML Server"
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
