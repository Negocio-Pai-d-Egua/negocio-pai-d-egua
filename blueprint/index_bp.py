from flask import Blueprint, render_template

index_bp= Blueprint("index", __name__, template_folder="templates")

@index_bp.route("/")
def home():
    return render_template("index.html")

@index_bp.route("/combinado",methods= ["post"])
def combinado():

    return render_template("Comida/combinado_1.html",combinado=combinado,preco=preco,src=src,descricao=descricao)