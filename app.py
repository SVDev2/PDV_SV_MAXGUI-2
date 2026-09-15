from flask import Flask, render_template
from dados.banco import *

app = Flask(__name__)

app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.after_request
def add_header(response):
    response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    return response

@app.route("/")
def inicio():
    return render_template("inicio.html")

@app.route("/sobre")
def sobre():
    return render_template("sobre.html")

@app.route("/entrar")
def entrar():
    return render_template("auth/entrar.html")

@app.route("/cadastrar")
def cadastrar():
    return render_template("auth/cadastrar.html")

@app.route("/privacidade")
def privacidade():
    return render_template("privacidade.html")

@app.route("/termos")
def termos():
    return render_template("termos.html")

@app.route("/doacao")
def doacao():
    return render_template("doacao.html")

@app.route("/configuracoes")
def configuracoes():
    return render_template("configuracoes/configuracoes.html")

@app.route("/rotas")
def rotas():
    return render_template("internal/rotas.html")

@app.route("/cookies")
def cookies():
    return render_template("cookies.html")

@app.route("/banner")
def banner():
    return render_template("includes/banner_cookies.html")

@app.route("/redefinir-senha")
def recuparaS():
    return render_template("auth/recupera_senha.html")

@app.route("/propagandas-slide")
def slide():
    return render_template("includes/propagandas_slide.html")

@app.route("/desenvolvimento")
def desenvolvimento():
    return render_template("includes/em_desenvolvimento.html")

@app.route("/401")
def error401():
    return render_template("erros/401.html")

@app.route("/403")
def error403():
    return render_template("erros/403.html")

@app.route("/404")
def error404():
    return render_template("erros/404.html")

@app.route("/410")
def error410():
    return render_template("erros/410.html")

@app.route("/500")
def error500():
    return render_template("erros/500.html")

@app.route("/502")
def error502():
    return render_template("erros/502.html")

@app.route("/503")
def error503():
    return render_template("erros/503.html")

@app.route("/504")
def error504():
    return render_template("erros/504.html")

@app.route("/header")
def header():
    return render_template("includes/header.html")

@app.route("/sites-SV")
def sitesSV():
    return render_template("sites_SV.html")

@app.route("/relatorio-interno-sv")
def internal_report():
    return render_template("internal/internal_report.html")

if __name__ == "__main__":
    banco_caixa()
    app.run(debug=True, host="127.0.0.1", port=5000)