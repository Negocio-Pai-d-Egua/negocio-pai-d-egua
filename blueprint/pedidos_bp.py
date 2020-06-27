from flask import Blueprint, render_template, request, current_app
from config.model import Produto, Carrinho, Pedidos
from config.serealizer import ProdutoSchema, CarrinhoSchema, PedidoSchema

pedidos_bp= Blueprint("pedido", __name__, template_folder="templates")

@pedidos_bp.route("/create_pedido", methods= ["post"])
def create_pedido():
    pedido = PedidoSchema()
    pedidos= Pedidos()
    current_app.db.session.add(pedidos)
    current_app.db.session.commit()
    return "OK"

@pedidos_bp.route("/read_pedido")
def read_pedido():
    pedido=PedidoSchema(many=True)
    result= Pedidos.query.all()
    return pedido.jsonify(result)

@pedidos_bp.route("/update_pedido")
def update_pedido():
    id = request.args.get('id')
    pedido = PedidoSchema(many=True)
    query= Pedidos.query.filter(pedido.id==id)
    query.update(request.json)
    current_app.db.session.commit()
    return ...

@pedidos_bp.route("/delete_pedido")
def delete_pedido():
    id = request.args.get('id')
    pedido = PedidoSchema(many=True)
    Pedidos.query.filter(pedido.id == id).delete()
    current_app.db.session.commit()
    return ...