from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import LoginManeger

login_bp = Blueprint("login", __name__)

@login_bp.route("/entrar")
def entrar():
    return render_template("auth/entrar.html")

@login_bp.route("/cadastrar")
def cadastrar():
    return render_template("auth/cadastrar.html")

@login_bp.route("/redefinir-senha")
def recuparaS():
    return render_template("auth/recupera_senha.html")