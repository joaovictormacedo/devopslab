from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "Olá, essa é minha aplicação em Python e Flask"

if __name__ == '__main__':
    app.run()