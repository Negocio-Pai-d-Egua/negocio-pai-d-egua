from flask import Blueprint, render_template
validacao_compra_bp = Blueprint("validacao_compra", __name__, template_folder="templates")


@validacao_compra_bp.route("/validacao_compra",methods= ["post"])
def validacao_compra():

    return ...

@validacao_compra_bp.route("/carrinho")
def carrinho():

    return render_template("carrinho.html")

@validacao_compra_bp.route("/pedido_finalizado", methods= ["post"])
def pedido_finalizado():

    return render_template("pedido_finalizado.html")

@validacao_compra_bp.route("/formulario", methods= ["post"])
def formulario():
    return render_template("formulario.html")