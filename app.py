from flask import Flask, render_template
from managers.configuracoes import carregar_versao
############
from blueprints.mensagens.errors import errors_bp
from blueprints.interno.interno import intern_bp
from blueprints.login_register.login_register import login_bp
############
app = Flask(__name__)
app.register_blueprint(errors_bp)
app.register_blueprint(intern_bp)
app.register_blueprint(login_bp)

#app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

#@app.after_request
#def add_header(response):
#    response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
#    response.headers["Pragma"] = "no-cache"
#    response.headers["Expires"] = "0"
#    return response
    
@app.context_processor
def info_globais():
    return {"versao": carregar_versao()}

@app.route("/")
def home():
    return render_template("inicio.html")

@app.route("/sobre")
def sobre():
    return render_template("sobre.html")

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

@app.route("/cookies")
def cookies():
    return render_template("cookies.html")

@app.route("/desenvolvimento")
def desenvolvimento():
    return render_template("includes/em_desenvolvimento.html")

@app.route("/sites-SV")
def sitesSV():
    return render_template("sites_SV.html")

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)