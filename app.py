from flask import Flask, request, render_template
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        resposta1 = request.form.get("resposta1")
        resposta2 = request.form.get("resposta2")

        with open("respostas.txt", "a", encoding="utf-8") as f:
            f.write(f"Propósito: {resposta1}\nDesejo: {resposta2}\n---\n")

        return render_template("index.html", enviado=True)

    return render_template("index.html", enviado=False)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)