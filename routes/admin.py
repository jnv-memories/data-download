from flask import Blueprint, jsonify, send_file
from pathlib import Path

admin_bp = Blueprint("admin", __name__, url_prefix="/admin")


DETAILS_XML = Path("details.xml")
TEACHER_XML = Path("teacher_details.xml")


@admin_bp.get("/health")
def health():
    return jsonify({"status": "ok"})


@admin_bp.get("/download/details")
def download_details():

    if not DETAILS_XML.exists():
        return jsonify({"error": "details.xml not found"}), 404

    return send_file(
        DETAILS_XML,
        as_attachment=True,
        download_name="details.xml",
        mimetype="application/xml"
    )


@admin_bp.get("/download/teacher")
def download_teacher():

    if not TEACHER_XML.exists():
        return jsonify({"error": "teacher_details.xml not found"}), 404

    return send_file(
        TEACHER_XML,
        as_attachment=True,
        download_name="teacher_details.xml",
        mimetype="application/xml"
    )
