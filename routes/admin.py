from flask import Blueprint
from flask import jsonify
from flask import request

from routes.generator import generate_xml
from services.pw_api import upload_file

admin_bp = Blueprint("admin", __name__, url_prefix="/admin")


@admin_bp.get("/health")
def health():

    return jsonify({
        "status": "ok"
    })


@admin_bp.post("/generate")

def generate():

    body = request.json or {}

    users = body.get("users", [])

    xml_path = generate_xml(users)

    upload_result = upload_file(xml_path)

    return jsonify({
        "xml": xml_path,
        "upload": upload_result
    })
