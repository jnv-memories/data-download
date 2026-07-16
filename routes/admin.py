from flask import Blueprint, jsonify, send_file, request
from pathlib import Path

from get_phonenumber import save, get_user
from get_faculty_number import teacher

admin_bp = Blueprint("admin", __name__, url_prefix="/admin")

DETAILS_XML = Path("details.xml")
TEACHER_XML = Path("teacher_details.xml")


@admin_bp.get("/health")
def health():
    return jsonify({
        "status": "ok"
    })


@admin_bp.post("/save")
def save_users():
    """
    POST /admin/save
    POST /admin/save?unfollow=true
    """

    unfollow = (
        request.args.get("unfollow", "false").lower() == "true"
    )

    total = save(unfollow)

    return jsonify({
        "success": True,
        "processed": total,
        "unfollow": unfollow
    })


@admin_bp.post("/community")
def community():
    """
    POST /admin/community

    {
        "community_id":"xxxxx",
        "page":1
    }
    """

    body = request.get_json(silent=True)

    if not body:
        return jsonify({
            "success": False,
            "error": "JSON body required."
        }), 400

    comm_id = body.get("community_id")
    page = body.get("page")

    if not comm_id or page is None:
        return jsonify({
            "success": False,
            "error": "community_id and page are required."
        }), 400

    total = get_user(comm_id, str(page))

    return jsonify({
        "success": True,
        "processed": total,
        "community_id": comm_id,
        "page": page
    })


@admin_bp.post("/teacher")
def teacher_endpoint():
    """
    POST /admin/teacher
    """

    total = teacher()

    return jsonify({
        "success": True,
        "processed": total
    })


@admin_bp.get("/download/details")
def download_details():

    if not DETAILS_XML.exists():
        return jsonify({
            "success": False,
            "error": "details.xml not found"
        }), 404

    return send_file(
        DETAILS_XML,
        as_attachment=True,
        download_name="details.xml",
        mimetype="application/xml"
    )


@admin_bp.get("/download/teacher")
def download_teacher():

    if not TEACHER_XML.exists():
        return jsonify({
            "success": False,
            "error": "teacher_details.xml not found"
        }), 404

    return send_file(
        TEACHER_XML,
        as_attachment=True,
        download_name="teacher_details.xml",
        mimetype="application/xml"
    )