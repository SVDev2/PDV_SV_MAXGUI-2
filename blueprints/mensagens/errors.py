from flask import Blueprint, render_template

errors_bp = Blueprint("errors", __name__)

@errors_bp.app_errorhandler(400)
def error400(e):
    return render_template("erros/400.html"), 400

@errors_bp.app_errorhandler(401)
def error401(e):
    return render_template("erros/401.html"), 401

@errors_bp.app_errorhandler(403)
def error403(e):
    return render_template("erros/403.html"), 403

@errors_bp.app_errorhandler(404)
def error404(e):
    return render_template("erros/404.html"), 404

@errors_bp.app_errorhandler(408)
def error408(e):
    return render_template("erros/408.html"), 408

@errors_bp.app_errorhandler(410)
def error410(e):
    return render_template("erros/410.html"), 410

@errors_bp.app_errorhandler(423)
def error423(e):
    return render_template("erros/423.html"), 423

@errors_bp.app_errorhandler(429)
def error429(e):
    return render_template("erros/429.html"), 429

@errors_bp.app_errorhandler(500)
def error500(e):
    return render_template("erros/500.html"), 500

@errors_bp.app_errorhandler(502)
def error502(e):
    return render_template("erros/502.html"), 502

@errors_bp.app_errorhandler(503)
def error503(e):
    return render_template("erros/503.html"), 503

@errors_bp.app_errorhandler(504)
def error504(e):
    return render_template("erros/504.html"), 504