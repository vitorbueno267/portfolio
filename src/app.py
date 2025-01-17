from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    title = "Home"
    return render_template("index.html", title=title)


@app.route("/sobremim")
def sobremim():
    title = "Sobre mim"
    return render_template("sobre-mim.html", title=title)


@app.route("/projetos")
def projetos():
    title = "Projetos"
    return render_template("projetos.html", title=title)


@app.route("/contato")
def contato():
    title = "Contato"
    return render_template("contato.html", title=title)


if __name__ == "__main__":
    app.run(debug=True)