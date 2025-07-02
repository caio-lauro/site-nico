from flask import Flask, request, render_template, Response
import os
import requests

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        resposta1 = request.form.get("resposta1")
        resposta2 = request.form.get("resposta2")

        # Salvar localmente
        with open("respostas.txt", "a", encoding="utf-8") as f:
            f.write(f"Propósito: {resposta1}\nDesejo: {resposta2}\n---\n")

        return render_template("index.html", enviado=True)

    return render_template("index.html", enviado=False)

@app.route("/respostas")
def ver_respostas():
    senha = request.args.get("senha")
    if senha != "minhasenha123":
        return "Acesso negado", 403

    if not os.path.exists("respostas.txt"):
        return "Nenhuma resposta ainda."

    with open("respostas.txt", "r", encoding="utf-8") as f:
        conteudo = f.read()
    return Response(conteudo, mimetype="text/plain")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)