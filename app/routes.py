from flask import Blueprint, render_template, request, send_file, jsonify, flash, redirect, url_for
from werkzeug.utils import secure_filename
from pathlib import Path
import uuid
import os

from .tools.pdf_tools import TOOL_REGISTRY, run_tool

main = Blueprint("main", __name__, static_folder="static", template_folder="templates")

@main.route("/")
def home():
    categories = {}
    for slug, meta in TOOL_REGISTRY.items():
        categories.setdefault(meta["category"], []).append((slug, meta))
    return render_template("index.html", categories=categories)

@main.route("/tool/<slug>", methods=["GET", "POST"])
def tool(slug):
    meta = TOOL_REGISTRY.get(slug)
    if not meta:
        return render_template("404.html"), 404

    if request.method == "POST":
        files = request.files.getlist("files")
        options = dict(request.form)
        valid = [f for f in files if f and f.filename]

        if not valid and meta.get("requires_file", True):
            flash("Please select the required file(s).", "error")
            return redirect(request.url)

        job_id = uuid.uuid4().hex
        saved = []
        for f in valid:
            name = secure_filename(f.filename)
            path = Path(main_app_config()["UPLOAD_FOLDER"]) / f"{job_id}_{name}"
            f.save(path)
            saved.append(path)

        try:
            result = run_tool(slug, saved, options, main_app_config()["OUTPUT_FOLDER"])
            if result and Path(result).exists():
                return send_file(result, as_attachment=True, download_name=Path(result).name)
            flash("This feature is ready in the DocGenius framework but needs its optional integration configured.", "info")
        except Exception as exc:
            flash(f"Tool error: {exc}", "error")

    return render_template("tool.html", slug=slug, meta=meta)

@main.route("/api/tools")
def api_tools():
    return jsonify([
        {"slug": slug, **meta}
        for slug, meta in TOOL_REGISTRY.items()
    ])

@main.route("/about")
def about():
    return render_template("about.html")

@main.route("/privacy")
def privacy():
    return render_template("privacy.html")

def main_app_config():
    from flask import current_app
    return current_app.config
