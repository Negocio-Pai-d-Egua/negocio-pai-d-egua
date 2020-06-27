from flask import Blueprint, render_template, request, current_app
from config.model import Produto, Carrinho
from config.serealizer import ProdutoSchema, CarrinhoSchema

produto_bp= Blueprint("produto", __name__, template_folder="templates")

@produto_bp.route("/create_produto", methods= ["post"])
def create_produto():
    print("teste")
    ps= ProdutoSchema()
    #carrinho_id= int(request.cookies.get("carrinho_id"))
    #carrinho_query= Carrinho.query.filter(Carrinho.id== carrinho_id).first()
    produto= request.json
    produto= ps.load(produto)
    current_app.db.session.add(produto)
    #carrinho_query.produtos.append(produto)
    current_app.db.session.commit()
    return "Ok"

@produto_bp.route("/read_produto")
def read_produto():
    ps=ProdutoSchema(many=True)
    result= Produto.query.all()
    return ps.jsonify(result)

@produto_bp.route("/update_produto")
def update_produto():
    id= request.args.get('id')
    ps=ProdutoSchema(many=True)
    query=Produto.query.filter(Produto.id==id)
    query.update(request.json)
    current_app.db.session.commit()
    return ...

@produto_bp.route("/delete_produto")
def delete_produto():
    id = request.args.get('id')
    ps = ProdutoSchema(many=True)
    Produto.query.filter(Produto.id == id).delete()
    current_app.db.session.commit()
    return ...

def criar_produto(novo_produto):
    ps= ProdutoSchema()
    produto= novo_produto
    produto= ps.load(produto)
    current_app.db.session.add(produto)
    current_app.db.session.commit()
    return produto.id
