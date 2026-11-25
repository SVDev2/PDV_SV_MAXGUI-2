from flask import Blueprint, render_template

intern_bp = Blueprint("intern", __name__)

@intern_bp.route("/rotas")
def rotas():
    return render_template("internal/rotas.html")

@intern_bp.route("/relatorio-interno-sv")
def internal_report():
    return render_template("internal/internal_report.html")