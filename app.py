from flask import Flask, render_template
from dados.banco import banco

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
    return render_template("entrar.html")
    
@app.route("/cadastrar")
def cadastrar():
    return render_template("cadastrar.html")
    
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
    return render_template("configuracoes.html")
    
@app.route("/rotas")
def rotas():
    return render_template("rotas.html")
    
@app.route("/cookies")
def cookies():
    return render_template("cookies.html")
    
@app.route("/banner")
def banner():
    return render_template("includes/banner_cookies.html")
    
@app.route("/redefinir-senha")
def recuparaS():
    return render_template("recupera_senha.html")
    
@app.route("/propagandas-slide")
def slide():
    return render_template("includes/propagandas_slide.html")
    
@app.route("/desenvolvimento")
def desenvolvimento():
    return render_template("includes/em_desenvolvimento.html")

if __name__ == "__main__":
    banco()
    app.run(debug=True, host="0.0.0.0", port=5000)